from channels.routing import URLRouter, ProtocolTypeRouter
from django.urls import path
from shoppingList.apps.notifier.consumers import NotificationsConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('notifications/', NotificationsConsumer)
    ])
})

