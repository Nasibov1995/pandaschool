from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from account.models import CustomUser
from exam.api.serializers import (ExamSerializer, ExamQuestionSerializer, ExamTypeSerializer,
                                  QuestionAnswerSerializer, ExamResultListSerializer, ExamResultCreateSerializer,
                                  ExamChooseTimeSerializer, StudentExamListSerializer)
from exam.models import Exam, ExamQuestion, QuestionAnswer, ExamResult, ExamType, StudentExam
from rest_framework import status


class ExamTypeListAPIView(ListAPIView):
    serializer_class = ExamTypeSerializer
    queryset = ExamType.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class ExamListAPIView(ListAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

    def get_queryset(self):
        return self.queryset.filter(exam_type__slug=self.kwargs['type'])


class ExamChooseTimeAPIView(CreateAPIView):
    serializer_class = ExamChooseTimeSerializer
    queryset = StudentExam.objects.all()
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        exam = ExamType.objects.get(pk=self.kwargs['pk'])
        student = CustomUser.objects.get(email=self.request.user.email)
        serializer.save(exam=exam, student=student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ExamUpdateTimeAPIView(UpdateAPIView):
    serializer_class = ExamChooseTimeSerializer
    queryset = StudentExam.objects.all()
    lookup_field = 'pk'


class ExamQuestionListAPIView(ListAPIView):
    serializer_class = ExamQuestionSerializer
    queryset = ExamQuestion.objects.all()

    def get_queryset(self):
        return self.queryset.filter(exam_questions__pk=self.kwargs['pk'])


class QuestionAnswerListAPIView(ListAPIView):
    serializer_class = QuestionAnswerSerializer
    queryset = QuestionAnswer.objects.all()

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs['pk'])


class ExamResultListAPIView(ListAPIView):
    serializer_class = ExamResultListSerializer
    queryset = ExamResult.objects.all()

    def get_queryset(self):
        return self.queryset.filter(student_exam__student__pk=self.kwargs['pk'])


class ExamResultCreateAPIView(CreateAPIView):
    serializer_class = ExamResultCreateSerializer
    queryset = ExamResult.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        student_exam = StudentExam.objects.get(pk=self.kwargs['pk'])
        student_exam.is_finished = True
        serializer.save(student_exam=student_exam)
        student_exam.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentExamListAPIView(ListAPIView):
    serializer_class = StudentExamListSerializer
    queryset = StudentExam.objects.all()

    def get_queryset(self):
        return self.queryset.filter(student=self.request.user)
