from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)

    def __str__(self):
        return self.name
    
class Transaction(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transactions')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.category.name.capitalize()} - {self.amount}"

class Budget(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budget')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category.name.capitalize()} - {float(self.amount)}"