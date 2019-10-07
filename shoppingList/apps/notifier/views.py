from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Notifications
from rest_framework import status
from django.utils import timezone
from shoppingList.helpers.response import success_response
from .serializers import NotificationsSerializer


class NotificationsPage(TemplateView):
    """
    view for displaying notifictions
    """
    template_name = 'notifications.html'


class ShowNotifictionsAPIView(ListAPIView):
    """
    view for retieving notifications
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationsSerializer

    def list(self, request):
        """
        display all notifications
        """
        notifications = Notifications.objects.filter(owner=request.user)
        for notification in notifications:  # set all objects as read
            if not notification.read:
                notification.read_at = timezone.now()
                notification.read = True
                notification.save()
            else:
                notification.delete()
                continue
        serializer = self.serializer_class(notifications, many=True)
        data = serializer.data
        return success_response(
            'All notifications',
            data,
            status_code=status.HTTP_200_OK
        )
