from django.urls import path
from resources import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    path('expenses/', views.expense_list),
    path('expenses/category/<int:pk>', views.category_expenses),
    path('expenses/<int:pk>/', views.expense_detail)
]