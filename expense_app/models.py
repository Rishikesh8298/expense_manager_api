from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Expense(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=200)
    description = models.TextField(default="")
    date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.userid) + " -> " + str(self.category) + " -> " + str(self.date)


class Category(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.userid) + " -> " + str(self.name)
