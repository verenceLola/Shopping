"""register the signal handler"""

from django.apps import AppConfig


class ShoppingItemConfig(AppConfig):
    """define the app config"""

    name = 'shoppingList.apps.shoppingItems'

    def ready(self):
        """register the signal handler when the app is ready"""

        import shoppingList.apps.shoppingItems.signals  # noqa


default_app_config = 'shoppingList.apps.shoppingItems.ShoppingItemConfig'
