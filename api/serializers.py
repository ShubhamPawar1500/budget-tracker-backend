from rest_framework import serializers
from .models import Note, Category, Transaction, Budget

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'owner']
        read_only_fields = ['owner']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

class TransactionSerializer(serializers.ModelSerializer):
    categoryId = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    amount = serializers.FloatField()

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'description', 'categoryId', 'date', 'owner']
        read_only_fields = ['owner']

class BudgetSerializer(serializers.ModelSerializer):
    categoryId = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    amount = serializers.FloatField()

    class Meta:
        model = Budget
        fields = ['id', 'categoryId', 'amount']
