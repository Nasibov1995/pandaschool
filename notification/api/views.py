from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from notification.api.serializers import NotificationSerializer, NotificationUpdateSerializer
from notification.models import NotificationModel
from rest_framework.response import Response
from rest_framework import status
from notification.api.permissions import IsSuperUser


class NotificationListAPIView(ListAPIView):
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsSuperUser,)


class NotificationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationUpdateSerializer
    permission_classes = (IsSuperUser,)
    lookup_field = "id"
