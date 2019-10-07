from django.db.models.signals import post_save
from django.dispatch import receiver
from shoppingList.apps.shoppingItems.models import Item, ShoppingList


@receiver(post_save, sender=Item)
def buy_shopping_item(sender, **kwargs):
    """
    deduct item amount from shopping list budget upon buying an item
    """
    instance = kwargs.get('instance')
    shopping_lists = instance.shoppinglist_set.values()
    for shopping_list in shopping_lists:
        # update item price fin each shopping list accordingly
        id = shopping_list.get('id')
        shopping_list_inst = ShoppingList.objects.get(pk=id)
        shopping_list_inst.budget = shopping_list_inst.budget - \
            instance.price if instance.bought else shopping_list_inst.\
            budget + instance.price
        shopping_list_inst.save()
