from django.urls import path, include
from . import views

urlpatterns = [
    #budgets urls
    path('budget/', views.BudgetsListCreate.as_view(), name='budget'),
    path('budget-details/<int:pk>/', views.BudgetDetails.as_view(), name='budget_details'),

    #budget incomes & expenses
    path('budget-income/', views.BudgetIncome.as_view(), name='budget_income'),
    path('budget-income-details/', views.BudgetIncomeDetails.as_view(), name='budget_income_details'),
    path('budget-expense/', views.BudgetExpense.as_view(), name='budget_expense'),
    path('budget-expense-details/', views.BudgetExpenseDetails.as_view(), name='budget_expense_details'),

    #budgets models urls
    path('budget-model/', views.BudgetModelsListCreate.as_view(), name='budget_model'),
    path('budget-model-details/<int:pk>/', views.BudgetModelsDetails.as_view(), name='budget_model_details'),

    #budget model incomes & expenses
    path('budget-model-income/', views.ModelIncome.as_view(), name='model_income'),
    path('budget-model-income-details/', views.ModelIncome.as_view(), name='model_income_details'),
    path('budget-model-expense/', views.ModelExpense.as_view(), name='model_expense'),
    path('budget-model-expense-details/', views.ModelExpense.as_view(), name='model_expense_details'),

    #income & expenses categories
    path('income-categories/', views.IncomeCategories.as_view(), name='income_categories'),
    path('expense-categories/', views.ExpenseCategories.as_view(), name='expense_categories')
]