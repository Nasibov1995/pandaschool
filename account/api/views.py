from account.models import CustomUser
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAdminUser


class CreateCustomUserAPIView(CreateAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
        })


class CustomUserListAPIView(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_student=True)


class AccountantListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return self.queryset.filter(is_accountant=True)


class CustomUserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'email'

    def get_queryset(self):
        return self.queryset.filter(email=self.kwargs['email'])
