from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from service.models import (
    MonthModel, TeacherPaymentInformationModel, StudentPaymentInformationModel
)
from service.api.serializers import (
    MonthSerializer, TeacherPaymentInformationSerializer, TeacherPaymentInformationUpdateSerializer,
    StudentPaymentInformationSerializer, StudentPaymentInformationUpdateSerializer
)


class SeasonMonthListAPIView(ListAPIView):
    def get_queryset(self):
        season_id = self.kwargs["id"]
        return MonthModel.objects.filter(
            season_id=season_id
        )
    serializer_class = MonthSerializer


class TeacherMonthPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        month_id = self.kwargs["id"]
        return TeacherPaymentInformationModel.objects.filter(
            month_id=month_id
        )
    serializer_class = TeacherPaymentInformationSerializer


class MonthTeacherPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        teacher_id = self.kwargs["id"]
        return TeacherPaymentInformationModel.objects.filter(
            teacher_id=teacher_id
        )
    serializer_class = TeacherPaymentInformationSerializer


class TeacherPaymentInformationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = TeacherPaymentInformationModel.objects.all()
    serializer_class = TeacherPaymentInformationUpdateSerializer
    lookup_field = "id"


class StudentMonthPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        month_id = self.kwargs.get("month_id")
        return StudentPaymentInformationModel.objects.filter(
            month_id=month_id
        )
    serializer_class = StudentPaymentInformationSerializer


class StudentCategoryMonthPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        month_id = self.kwargs.get("month_id")
        category_id = self.kwargs.get("category_id")
        return StudentPaymentInformationModel.objects.filter(
            category=category_id,
            month_id=month_id
        )
    serializer_class = StudentPaymentInformationSerializer


class MonthStudentPaymentInformationListAPIView(ListAPIView):
    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        category_id = self.kwargs['category_id']
        return StudentPaymentInformationModel.objects.filter(
            student_id=student_id,
            category=category_id
        )
    serializer_class = StudentPaymentInformationSerializer


class StudentPaymentInformationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = StudentPaymentInformationModel.objects.all()
    serializer_class = StudentPaymentInformationUpdateSerializer
    lookup_field = "id"
