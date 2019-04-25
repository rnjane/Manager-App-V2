from django.urls import path, include
from . import views

urlpatterns = [
    #budgets urls
    path('budget/', views.BudgetsListCreate.as_view(), name='budget'),
    path('budget-details/<int:pk>/', views.BudgetDetails.as_view(), name='budget_details'),

    #budgets models urls
    path('budget-model/', views.BudgetModelsListCreate.as_view(), name='budget_model'),
    path('budget-model-details/<int:pk>/', views.BudgetModelsDetails.as_view(), name='budget_model_details'),
]