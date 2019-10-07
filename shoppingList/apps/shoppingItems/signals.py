from django.db.models.signals import post_save
from django.dispatch import receiver
from shoppingList.apps.shoppingItems.models import Item, ShoppingList
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from shoppingList.helpers.notifications import save_notification


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
        list_instance = ShoppingList.objects.get(pk=id)
        list_instance.budget = list_instance.budget - \
            instance.price if instance.bought else list_instance.\
            budget + instance.price
        list_instance.save()
        save_notification(
            "Shopping List {} Budget Updated to {}".format(list_instance.name, list_instance.budget),  # noqa
            'BUDGET UPDATED',
            instance.owner
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "budget", {
                "type": "budget",
                "event": "Shopping List {} Budget Updated".format(list_instance.name),  # noqa
                "new_budget": list_instance.budget
            }
        )
