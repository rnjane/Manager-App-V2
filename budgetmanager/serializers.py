from rest_framework import serializers
from . import models

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = ('name', 'incomes', 'expenses', 'date_created')


class BudgetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BudgetModel
        fields = ('budget_model_name', 'date_created', 'current')


class ModelIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelIncome
        fields = ('model_income_name', 'model_income_amount', 'budget_model')


class ModelExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelExpense
        fields = ('model_expense_name', 'model_expense_amount', 'budget_model')


class BudgetExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BudgetExpense
        fields = ('name', 'amount', 'category', 'description', 'date_created', 'budget')


class BudgetIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BudgetIncome
        fields = ('name', 'amount', 'category', 'description', 'date_created', 'budget')


class IncomeCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IncomeCategories
        fields = ('name', 'amount', 'owner')


class ExpenseCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpenseCategories
        fields = ('name', 'amount', 'owner')