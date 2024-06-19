from django.contrib import admin

from .models import CustomUser, Exam, ExamQuestion, ExamType, QuestionAnswer, ExamResult, StudentAnswer, StudentExam

admin.site.site_header = "Online Exam System"
admin.site.site_title = "Online Exam System"



@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    search_fields = ['answer']
    list_display = ['__str__', 'answer_variant', 'is_correct']
    list_filter = ['is_correct']
    list_per_page = 15

    change_list_template = 'admin/questionanswer/change_list.html'

    def get_exams(self, request):
        return Exam.objects.all()

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['exams'] = self.get_exams(request)
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(ExamQuestion)
class ExamQuestionAdmin(admin.ModelAdmin):
    search_fields = ['question']
    autocomplete_fields = ['answers']
    list_per_page = 15

    change_list_template = 'admin/examquestion/change_list.html'

    def get_exams(self, request):
        return Exam.objects.all()

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['exams'] = self.get_exams(request)
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['exam_name', 'variant']
    list_per_page = 20
    search_fields = ['exam_name']

    fieldsets = [
        ('General Information', {
            'fields': ['exam_type', 'variant', 'exam_name', 'questions'],
        }),
        ('Reading and Listening', {
            'fields': ['reading', 'listening'],
            'classes': ['tab_reading_listening'],
        })
    ]

    autocomplete_fields = ['questions']


@admin.register(ExamType)
class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_status', 'exam_duration']
    list_per_page = 20
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(StudentExam)
class StudentExamAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_exam_datetime', 'is_finished']
    list_per_page = 20
    search_fields = ['exam', 'student', 'is_finished']


admin.site.register(ExamResult)
admin.site.register(StudentAnswer)
