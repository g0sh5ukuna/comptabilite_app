from django.contrib import admin
from .models import Account, Transaction, JournalEntry

# Configuration de l'affichage du modèle Account dans l'interface d'administration
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'type', 'balance')  # Colonnes affichées dans la liste
    search_fields = ('code', 'title')  # Champs de recherche
    list_filter = ('type',)  # Filtres disponibles dans la barre latérale

# Configuration de l'affichage du modèle Transaction dans l'interface d'administration
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'debit_account', 'credit_account', 'amount', 'user')
    search_fields = ('description', 'debit_account__title', 'credit_account__title')
    list_filter = ('date', 'user')

# Configuration de l'affichage du modèle JournalEntry dans l'interface d'administration
@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'created_at', 'user')
    search_fields = ('transaction__description', 'user__username')
    list_filter = ('created_at', 'user')

    # Ajouter des champs en lecture seule dans le formulaire d'édition
    readonly_fields = ('created_at',)
