from rest_framework import serializers
from .models import Account, Transaction, JournalEntry

class AccountSerializer(serializers.ModelSerializer):
    """ Sérializer pour le modèle Account avec affichage du solde formaté """

    formatted_balance = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ['id', 'title', 'code', 'type', 'balance', 'formatted_balance']
    
    def get_formatted_balance(self, obj):
        """ Retourne le solde formaté avec deux décimales et un séparateur de milliers """
        return f"{obj.balance:,.2f} €"

class TransactionSerializer(serializers.ModelSerializer):
    """ Sérializer pour le modèle Transaction avec validations et affichage des noms de comptes """

    debit_account_name = serializers.CharField(source='debit_account.title', read_only=True)
    credit_account_name = serializers.CharField(source='credit_account.title', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'date', 'description', 'debit_account', 'debit_account_name', 
                  'credit_account', 'credit_account_name', 'amount', 'user']
    
    def validate(self, data):
        """ Vérification des règles comptables avant enregistrement """
        debit_account = data.get('debit_account')
        credit_account = data.get('credit_account')
        amount = data.get('amount')

        if amount <= 0:
            raise serializers.ValidationError("Le montant de la transaction doit être positif.")

        if debit_account == credit_account:
            raise serializers.ValidationError("Le compte débité et crédité doivent être différents.")

        return data

class JournalEntrySerializer(serializers.ModelSerializer):
    """ Sérializer pour le modèle JournalEntry avec affichage du nom de l'utilisateur """
    
    transaction_description = serializers.CharField(source='transaction.description', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = JournalEntry
        fields = ['id', 'transaction', 'transaction_description', 'created_at', 'user', 'user_name']
