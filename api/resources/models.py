from importlib.metadata import requires
from unicodedata import category
from django.db import models

class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=50)
    user = models.TextField()


class Expense(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=50)
    amount = models.IntegerField()
    date = models.DateField()
    category_id = models.IntegerField(default=0)
    user = models.TextField()
