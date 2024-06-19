from django.urls import path
from accounting.api import views

urlpatterns = [
    path('season-month-list/<int:id>/',
         views.SeasonMonthListAPIView.as_view(), name="month-list"),
    path('teacher-month-payment-list/<int:id>/',
         views.TeacherMonthPaymentInformationListAPIView.as_view(), name="teacher-month-payment-list"),
    path('month-teacher-payment-list/<int:id>/',
         views.MonthTeacherPaymentInformationListAPIView.as_view(), name="month-teacher-payment-list"),
    path('teacher-payment-retrieve-update/<int:id>/',
         views.TeacherPaymentInformationRetrieveUpdateAPIView.as_view(), name="teacher-payment-retrieve-update"),
    path('student-month-payment-list/<int:month_id>/',
         views.StudentMonthPaymentInformationListAPIView.as_view(), name="student-month-payment-list"),
    path('month-student-payment-list/<int:student_id>/<int:category_id>/',
         views.MonthStudentPaymentInformationListAPIView.as_view(), name="month-student-payment-list"),
    path('student-payment-retrieve-update/<int:id>/',
         views.StudentPaymentInformationRetrieveUpdateAPIView.as_view(), name="student-payment-retrieve-update"),
    path('student-category-month-payment-list/<int:category_id>/<int:month_id>/',
         views.StudentCategoryMonthPaymentInformationListAPIView.as_view(), name="student-category-month-payment-list"),
]
