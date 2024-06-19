from django.urls import path
from exam.api.views import (ExamTypeListAPIView, ExamListAPIView, ExamResultListAPIView,
                            ExamResultCreateAPIView, ExamChooseTimeAPIView, StudentExamListAPIView,
                            ExamUpdateTimeAPIView)

urlpatterns = [
    path("exam-types/", ExamTypeListAPIView.as_view(), name="exams"),
    path("<slug:type>/exams/", ExamListAPIView.as_view(), name="exams"),
    path("student-exams/", StudentExamListAPIView.as_view(), name="student-exams"),
    path("student-exam/<int:pk>/result/",
         ExamResultCreateAPIView.as_view(), name="student-result"),
    path("student/<int:pk>/results/",
         ExamResultListAPIView.as_view(), name="student-results"),
    path("create-exam/<int:pk>/",
         ExamChooseTimeAPIView.as_view(), name="exam-create"),
    path("update-exam/<int:pk>/",
         ExamUpdateTimeAPIView.as_view(), name="exam-update"),
]
