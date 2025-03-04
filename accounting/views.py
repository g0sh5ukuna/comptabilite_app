import logging
from django.db.models import Sum
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
import openpyxl
from openpyxl.utils import get_column_letter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from .models import Account, Transaction, JournalEntry
from .serializers import AccountSerializer, TransactionSerializer, JournalEntrySerializer

# 📌 Configuration des logs
logger = logging.getLogger(__name__)

# ✅ Gestion des comptes comptables
class AccountViewSet(viewsets.ModelViewSet):
    """
    CRUD des comptes comptables
    - 🔍 GET /accounts/ → Lister les comptes
    - ➕ POST /accounts/ → Créer un compte
    - 📝 PUT /accounts/{id}/ → Modifier un compte
    - ❌ DELETE /accounts/{id}/ → Supprimer un compte
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Liste des comptes comptables",
        responses={200: AccountSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        logger.info("Liste des comptes consultée par %s", request.user)
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Créer un nouveau compte comptable",
        request_body=AccountSerializer,
        responses={201: AccountSerializer}
    )
    def create(self, request, *args, **kwargs):
        logger.info("Création d'un compte par %s", request.user)
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Modifier un compte comptable",
        request_body=AccountSerializer,
        responses={200: AccountSerializer}
    )
    def update(self, request, *args, **kwargs):
        logger.info("Modification du compte %s par %s", kwargs['pk'], request.user)
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Supprimer un compte comptable",
        responses={204: "Compte supprimé"}
    )
    def destroy(self, request, *args, **kwargs):
        logger.warning("Suppression du compte %s par %s", kwargs['pk'], request.user)
        return super().destroy(request, *args, **kwargs)

# CRUD des transactions
class TransactionViewSet(viewsets.ModelViewSet):
    """
    CRUD des transactions comptables
    - 🔍 GET /transactions/ → Lister les transactions
    - ➕ POST /transactions/ → Enregistrer une transaction (avec validation)
    - 📝 PUT /transactions/{id}/ → Modifier une transaction
    - ❌ DELETE /transactions/{id}/ → Supprimer une transaction (Admin only)
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'debit_account', 'credit_account']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        logger.info("Nouvelle transaction créée par %s", self.request.user)

    @swagger_auto_schema(
        operation_description="Supprimer une transaction (Admin seulement)",
        responses={204: "Transaction supprimée"}
    )
    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({"error": "Seuls les admins peuvent supprimer une transaction"},
                            status=status.HTTP_403_FORBIDDEN)
        logger.warning("Transaction %s supprimée par %s", kwargs['pk'], request.user)
        return super().destroy(request, *args, **kwargs)

# CRUD des écritures comptables
class ExportBalanceViewSet(viewsets.ViewSet):
    """
    📊 Export de la balance comptable en Excel
    - 📥 GET /export-balance/ → Télécharger un fichier Excel de la balance comptable
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Exporter la balance comptable sous format Excel",
        responses={200: "Fichier Excel téléchargé"}
    )
    @action(detail=False, methods=['get'])
    def export_balance(self, request):
        accounts = Account.objects.all()
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=balance_comptable.xlsx'

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Balance Comptable"
        headers = ["Compte", "Intitulé", "Solde début période", "Débit", "Crédit", "Solde fin période"]
        sheet.append(headers)

        for account in accounts:
            debits = Transaction.objects.filter(debit_account=account).aggregate(total=Sum('amount'))['total'] or 0
            credits = Transaction.objects.filter(credit_account=account).aggregate(total=Sum('amount'))['total'] or 0
            solde_initial = account.balance - (credits - debits)

            row = [account.code, account.title, solde_initial, debits, credits, account.balance]
            sheet.append(row)

        workbook.save(response)
        logger.info("Balance comptable exportée par %s", request.user)
        return response

class JournalEntryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API Read-Only pour consulter les entrées du journal comptable
    """
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
