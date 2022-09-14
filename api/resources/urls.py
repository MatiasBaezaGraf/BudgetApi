from django.urls import path
from resources import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<str:user>/', views.user_categories),
    path('categories/delete/<int:pk>/', views.delete_category),
    path('expenses/', views.expense_list),
    path('expenses/<str:user>/', views.user_expenses),
    path('expenses/delete/<int:pk>/', views.delete_expense),
    path('expenses/category/<int:pk>', views.category_expenses),
]