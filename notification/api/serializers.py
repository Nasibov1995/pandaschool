from rest_framework import serializers
from notification.models import NotificationModel

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = "__all__"

class NotificationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = ("status",)