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


#budget-models
class BudgetModelsListCreate(generics.ListCreateAPIView):
    queryset = models.BudgetModel.objects.all()
    serializer_class = serializers.BudgetModelSerializer

    def perform_create(self, serializer):
        serializer.save(budget_model_owner=self.request.user)


class BudgetModelsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BudgetModel.objects.all()
    serializer_class = serializers.BudgetModelSerializer