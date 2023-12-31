from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Sum

from . import models
from . import serializers
from . import paginations


class ExpenseListCreateAPI(generics.ListCreateAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = paginations.Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'date']
    search_fields = ['date', 'category']

    def get_queryset(self):
        users = self.request.user
        return models.Expense.objects.filter(userid=users)

    def perform_create(self, serializer):
        users = self.request.user
        serializer.save(userid=users)


class ExpenseGetUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = self.request.user
        return models.Expense.objects.filter(userid=users)


class CategoryListAPI(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = self.request.user
        return models.Category.objects.filter(userid=users)
