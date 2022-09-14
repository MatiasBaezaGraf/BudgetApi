from asyncore import read
from rest_framework import serializers
from resources.models import Category, Expense

class ExpenseSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Expense.objects.create(**validated_data)

    class Meta:
        model = Expense
        fields = ['id', 'name', 'amount', 'date', 'user', 'category_id']

class CategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    class Meta:
        model = Category
        fields = ['id', 'name', 'user']