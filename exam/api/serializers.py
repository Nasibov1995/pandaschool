from rest_framework import serializers
from account.api.serializers import CustomUserSerializer
from exam.models import (Exam, ExamQuestion, QuestionAnswer,
                         ExamResult, ExamType, StudentAnswer, StudentExam)


class QuestionAnswerSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = QuestionAnswer
        fields = ['id', 'question', 'answer_image',
                  'answer', 'answer_variant', 'is_correct']

    def get_question(self, obj):
        return obj.get_question().id


class ExamQuestionSerializer(serializers.ModelSerializer):
    answers = QuestionAnswerSerializer(many=True)

    class Meta:
        model = ExamQuestion
        fields = ['id', 'number', 'question_image',
                  'question', 'score', 'answers']


class ExamSerializer(serializers.ModelSerializer):
    questions = ExamQuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = ['id', 'variant', 'exam_name',
                  'reading', 'listening', 'questions']


class ExamListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ['id', 'variant']


class StudentAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentAnswer
        fields = ['question', 'selected_variant', 'given_answer']


class StudentExamSerializer(serializers.ModelSerializer):
    exam = serializers.StringRelatedField()
    student = serializers.StringRelatedField()

    class Meta:
        model = StudentExam
        fields = ['id', 'exam', 'student', 'exam_date', 'exam_time']


class ExamResultListSerializer(serializers.ModelSerializer):
    student_exam = StudentExamSerializer()
    student_answers = StudentAnswerSerializer(many=True)
    exam_answers = QuestionAnswerSerializer(many=True)

    class Meta:
        model = ExamResult
        fields = ['id', 'student_exam', 'student_answers', 'exam_answers',
                  'result', 'right_answers', 'wrong_answers']


class ExamResultCreateSerializer(serializers.ModelSerializer):
    student_answers = StudentAnswerSerializer(many=True)

    class Meta:
        model = ExamResult
        fields = ['student_answers']

    def create(self, validated_data):
        student_answers_data = validated_data.pop('student_answers', [])
        exam_result = ExamResult.objects.create(**validated_data)
        result = 0
        right_answers = 0
        wrong_answers = 0
        for student_answer_data in student_answers_data:
            question = ExamQuestion.objects.get(
                pk=student_answer_data['question'].pk)
            correct_answer = question.answers.get(is_correct=True)

            if correct_answer.answer_variant == student_answer_data['selected_variant'] or correct_answer.answer == student_answer_data['given_answer']:
                right_answers += 1
                result += question.score
            else:
                wrong_answers += 1

            selected_variant = student_answer_data['selected_variant']
            given_answer = student_answer_data['given_answer']
            exam_result.exam_answers.add(correct_answer)

            student_answer = StudentAnswer.objects.create(
                student=exam_result.student_exam.student,
                question=question,
                selected_variant=selected_variant,
                given_answer=given_answer
            )

            exam_result.student_answers.add(student_answer)

        exam_result.result = result
        exam_result.right_answers = right_answers
        exam_result.wrong_answers = wrong_answers
        exam_result.save()
        return exam_result


class ExamTypeSerializer(serializers.ModelSerializer):
    exams = serializers.SerializerMethodField()
    is_booked = serializers.SerializerMethodField()
    exam_time = serializers.SerializerMethodField()
    exam_date = serializers.SerializerMethodField()
    exam_id = serializers.SerializerMethodField()

    class Meta:
        model = ExamType
        fields = ['id', 'variant', 'name', 'slug', 'exam_status',
                  'is_booked', 'exam_id', 'exam_date', 'exam_time',
                  'exam_duration', 'exams']

    def get_exams(self, obj):
        exams = obj.exam_types.all()
        serialized_exams = ExamSerializer(exams, many=True).data
        return serialized_exams

    def get_is_booked(self, obj):
        user = self.context.get('user')
        if user:
            is_booked = StudentExam.objects.filter(
                exam=obj, student=user).exists()
            return is_booked
        return False

    def get_exam_time(self, obj):
        user = self.context.get('user')
        student_exam = StudentExam.objects.filter(
            exam=obj, student=user).first()
        if student_exam:
            return student_exam.exam_time
        return None

    def get_exam_date(self, obj):
        user = self.context.get('user')
        student_exam = StudentExam.objects.filter(
            exam=obj, student=user).first()
        if student_exam:
            return student_exam.exam_date
        return None

    def get_exam_id(self, obj):
        user = self.context.get('user')
        student_exam = StudentExam.objects.filter(
            exam=obj, student=user).first()
        if student_exam:
            return student_exam.pk
        return None


class StudentExamListSerializer(serializers.ModelSerializer):
    exam = ExamTypeSerializer()
    student = CustomUserSerializer()

    class Meta:
        model = StudentExam
        fields = ['id', 'exam', 'student',
                  'exam_date', 'exam_time', 'is_finished']


class ExamChooseTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExam
        fields = ['exam_time', 'exam_date']
