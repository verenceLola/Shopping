from django.db import models
from shoppingList.apps.account.models import User


class Item(models.Model):
    """
    Item model
    """
    name = models.CharField(max_length=10, blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self):
        """
        return string representtion of object
        """
        return self.name


class ShoppingList(models.Model):
    """
    Shopping List Model
    """
    desciption = models.CharField(max_length=266, blank=True)
    name = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now=True, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    budget = models.IntegerField(blank=False)

    def __str__(self):
        """
        return string representation of object
        """
        return self.name
