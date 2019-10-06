from django.db import models
from shoppingList.apps.account.models import User
from django.utils import timezone


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

    class Meta:
        """
        allow unique name per user
        """
        unique_together = (('owner', 'name'))

    description = models.CharField(max_length=266, blank=True)
    name = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    budget = models.IntegerField(default=0)

    def __str__(self):
        """
        return string representation of object
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        update timestamps
        """
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(ShoppingList, self).save(*args, **kwargs)
