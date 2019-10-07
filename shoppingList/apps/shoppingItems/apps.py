from django.apps import AppConfig


class ListConfig(AppConfig):
    name = 'shoppingItems'

    def ready(self):
        import shoppingItems.signals  # noqa
