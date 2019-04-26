from rest_framework import generics
from . import models, serializers

#budgets
class BudgetsListCreate(generics.ListCreateAPIView):
    queryset = models.Budget.objects.all()
    serializer_class = serializers.BudgetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BudgetDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Budget.objects.all()
    serializer_class = serializers.BudgetSerializer

#budget incomes &expenses
class BudgetIncome(generics.ListCreateAPIView):
    queryset = models.BudgetIncome.objects.all()
    serializer_class = serializers.BudgetIncomeSerializer


class BudgetIncomeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BudgetIncome.objects.all()
    serializer_class = serializers.BudgetIncomeSerializer


class BudgetExpense(generics.ListCreateAPIView):
    queryset = models.BudgetExpense.objects.all()
    serializer_class = serializers.BudgetExpenseSerializer


class BudgetExpenseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BudgetExpense.objects.all()
    serializer_class = serializers.BudgetExpenseSerializer


#budget-models
class BudgetModelsListCreate(generics.ListCreateAPIView):
    queryset = models.BudgetModel.objects.all()
    serializer_class = serializers.BudgetModelSerializer

    def perform_create(self, serializer):
        serializer.save(budget_model_owner=self.request.user)


class BudgetModelsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BudgetModel.objects.all()
    serializer_class = serializers.BudgetModelSerializer


#model income & expense
class ModelIncome(generics.ListCreateAPIView):
    queryset = models.ModelIncome.objects.all()
    serializer_class = serializers.ModelIncomeSerializer


class ModelIncomeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ModelIncome.objects.all()
    serializer_class = serializers.ModelIncomeSerializer


class ModelExpense(generics.ListCreateAPIView):
    queryset = models.ModelExpense.objects.all()
    serializer_class = serializers.ModelExpenseSerializer


class ModelExpenseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ModelExpense.objects.all()
    serializer_class = serializers.ModelExpenseSerializer


#incomes & expenses categories
class IncomeCategories(generics.ListAPIView):
    q1 = models.BudgetModel.objects.filter(current=True).first()
    queryset = models.ModelIncome.objects.filter(budget_model=q1)
    serializer_class = serializers.ModelIncomeSerializer


class ExpenseCategories(generics.ListAPIView):
    q1 = models.BudgetModel.objects.filter(current=True).first()
    queryset = models.ModelExpense.objects.filter(budget_model=q1)
    serializer_class = serializers.ModelExpenseSerializer