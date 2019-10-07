from shoppingList.apps.notifier.models import Notifications


def save_notification(message, type, owner):
    """
    save notification to user db
    """
    return Notifications.objects.create(
        message=message, notification_type=type,
        owner=owner
    )
