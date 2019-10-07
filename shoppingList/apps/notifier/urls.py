from django.urls import path
from .views import ShowNotifictionsAPIView

app_name = 'notifications'

urlpatterns = [
    path('notifications/', ShowNotifictionsAPIView.as_view(), name="notifications"),  # noqa
]
