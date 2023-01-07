from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.openDashboard),
    path('expenseform',views.openExpenseForm),
    path('incomeform',views.openIncomeForm),
    path('',views.openLoginForm),
    path('signup',views.openUserForm),
    path('register',views.registerUser),
    path('recordexpense',views.recordExpense),
    path('recordincome',views.recordIncome),
    path('fetchallexpenses',views.fetchAllExpenses),
    path('fetchallincomes',views.fetchAllIncomes),
    path('login',views.performLogin),
    path('logout',views.logout)
]