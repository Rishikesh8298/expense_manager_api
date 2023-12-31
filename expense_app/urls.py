from django.urls import path
from .apiviews import (ExpenseListCreateAPI,
                       ExpenseGetUpdateDestroyAPI,
                       CategoryListAPI)

urlpatterns = [
    path('expenses/', ExpenseListCreateAPI.as_view(), name='expenses-list-create'),
    path('expenses/<int:pk>/', ExpenseGetUpdateDestroyAPI.as_view(), name='expenses-get-update-destroy'),
    path('category/', CategoryListAPI.as_view(), name='category-list'),
]
