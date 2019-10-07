from rest_framework import serializers
from .models import Notifications


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('owner',)
        model = Notifications

    read_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False,)  # noqa
