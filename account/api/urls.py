from django.urls import path
from account.api.views import (
    AccountantListAPIView, CreateCustomUserAPIView, CustomUserListAPIView, CustomUserDetailAPIView)

urlpatterns = [

    path("create-user/", CreateCustomUserAPIView.as_view(), name="create-user"),
    path("students/", CustomUserListAPIView.as_view(), name="students"),
    path('accountants/', AccountantListAPIView.as_view(), name="accountants"),
    path("users/<str:email>/", CustomUserDetailAPIView.as_view(),
         name="user-detail"),
]
