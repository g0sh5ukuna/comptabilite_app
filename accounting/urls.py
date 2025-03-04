# accounting/urls.py
from django.urls import path, include, re_path  # Importation des fonctions de routage
from rest_framework.routers import DefaultRouter  # Importation du routeur par défaut
from rest_framework import permissions  # Importation des permissions REST
from drf_yasg.views import get_schema_view  # Importation de la vue de documentation
from drf_yasg import openapi  # Importation des outils de documentation Swagger / Redoc
from .views import AccountViewSet, TransactionViewSet, JournalEntryViewSet, ExportBalanceViewSet  # Importation des vues
# 📌 Configuration de la documentation Swagger / Redoc 
schema_view = get_schema_view(
    openapi.Info(
        title="API Gestion Comptable",
        default_version='v1',
        description="Documentation de l'API de gestion comptable avec Django REST Framework",
        terms_of_service="https://www.tonsite.com/terms/",
        contact=openapi.Contact(email="support@tonsite.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# 📌 Création du routeur pour les endpoints REST
router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')  # CRUD des comptes comptables
router.register(r'transactions', TransactionViewSet, basename='transaction')  # CRUD des transactions
router.register(r'journal', JournalEntryViewSet, basename='journal')  # Journal comptable
router.register(r'export-balance', ExportBalanceViewSet, basename='export-balance')  # Export Excel

# 📌 Définition des URLs
urlpatterns = [
    path('api/', include(router.urls)),  # Inclusion des routes API générées automatiquement

    # 📄 Documentation Swagger et ReDoc
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
