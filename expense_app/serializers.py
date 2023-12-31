from rest_framework import serializers
from . import models
from django.db.models import Sum


class ExpenseSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(max_length=150, read_only=True, source='userid.username')

    class Meta:
        model = models.Expense
        fields = '__all__'

    def save(self, **kwargs):
        user = self.context['request'].user
        category_name = self.validated_data.get('category')
        # Create or update the category
        existing_category = models.Category.objects.filter(userid=user, name=category_name)
        if len(existing_category) == 0:
            models.Category.objects.create(userid=user, name=category_name)

        # Set the user and save the Expense instance
        self.validated_data['userid'] = user
        instance = super().save(**kwargs)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    # userid = serializers.CharField(max_length=150, read_only=True, source='userid.username')
    total = serializers.SerializerMethodField()
    category = serializers.CharField(source='name')

    class Meta:
        model = models.Category
        fields = ['id', 'category', 'total']

    def get_total(self, obj):
        user = obj.userid
        category = obj.name
        total = (
                models.Expense.objects
                .filter(userid=user, category=category)
                .aggregate(Sum('amount'))
                ['amount__sum'] or 0
        )
        return total
