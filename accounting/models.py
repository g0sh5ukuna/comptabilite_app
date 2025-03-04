from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('Actif', 'Actif'),
        ('Passif', 'Passif'),
        ('Produit', 'Produit'),
        ('Charge', 'Charge'),
    )

    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.code} - {self.title}"

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    debit_account = models.ForeignKey(Account, related_name='debits', on_delete=models.CASCADE)
    credit_account = models.ForeignKey(Account, related_name='credits', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ajout du créateur de la transaction

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Le montant doit être positif.")
        if self.debit_account == self.credit_account:
            raise ValidationError("Le compte débité et crédité doivent être différents.")

    def save(self, *args, **kwargs):
        self.clean()  # Vérifier la validité avant sauvegarde
        super().save(*args, **kwargs)

        # Mise à jour des soldes
        self.debit_account.balance -= self.amount
        self.credit_account.balance += self.amount
        self.debit_account.save()
        self.credit_account.save()

    def __str__(self):
        return f"{self.description} ({self.amount}€)"

class JournalEntry(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur qui a enregistré

    def __str__(self):
        return f"Journal Entry for {self.transaction} by {self.user.username}"
