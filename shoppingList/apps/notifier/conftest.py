import pytest
from shoppingList.apps.notifier.models import Notifications


@pytest.fixture
def notication_creation(create_user):
    """
    test notification creation
    """
    owner = create_user
    details = {
        "message": "You've got  a message",
        "notification_type": "REFILL",
        "owner": owner
    }
    return Notifications.objects.create(**details)
