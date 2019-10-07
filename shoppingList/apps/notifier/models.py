from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Notifications(models.Model):
    """
    define the notification model for saving
    """
    sent_at = models.DateField(auto_now=True)
    message = models.CharField(max_length=256)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(default=None, null=True)
    REFILL_NOTIFICATION = 'REFILL'
    BELOW_THRESHOLD = "BELOW THRESHOLD"
    BUDGET_UPDATED = 'BUDGET UPDATED'
    NOTIFICATION_CHOICES = [
        (REFILL_NOTIFICATION, 'Refill shopping list budget'),
        (BELOW_THRESHOLD, 'Budget below set threshold'),
        (BUDGET_UPDATED, 'Budget updated')
    ]
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_CHOICES
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        """
        return message of notification
        """
        return self.message
