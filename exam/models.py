from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from account.models import CustomUser


class QuestionAnswer(models.Model):
    variants = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
    )
    answer_image = models.ImageField(
        upload_to="question_answers/", verbose_name="Şəkilli cavab", null=True, blank=True)
    answer = models.TextField(null=True, blank=True, verbose_name="Cavab")
    answer_variant = models.CharField(
        max_length=1, choices=variants, verbose_name="Variant", null=True, blank=True)
    is_correct = models.BooleanField(verbose_name="Düzgün cavab")

    def get_question(self):
        return self.question_answers.first()

    def __str__(self):
        if self.get_question():
            return f'{self.get_question().number}. sualın cavabı'
        return 'Sualın cavabı'

    class Meta:
        verbose_name = "Sualın Cavabı"
        verbose_name_plural = "Sualın Cavabları"


class ExamQuestion(models.Model):
    number = models.PositiveIntegerField(verbose_name="Sualın nömrəsi")
    question_image = models.ImageField(
        upload_to="exam_questions/", verbose_name="Sual", null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    score = models.PositiveIntegerField(verbose_name="Bal")
    answers = models.ManyToManyField(
        QuestionAnswer, verbose_name="Sualın Cavabları", related_name="question_answers", blank=True)

    def get_exam(self):
        return self.exam_questions.first()

    def __str__(self):
        if self.get_exam():
            return f"{self.get_exam().exam_name} - variant {self.get_exam().variant} imtahanının {self.number}. sualı"
        return f"{self.number}. sual"

    class Meta:
        verbose_name = "İmtahan sualı"
        verbose_name_plural = "İmtahan sualları"


class ExamType(models.Model):
    variant = models.CharField(max_length=1, verbose_name="Variant")
    name = models.CharField(max_length=50, verbose_name="İmtahan növü")
    slug = models.SlugField(
        max_length=50, verbose_name="İmtahan növü slug", null=True, blank=True)
    exam_status = models.BooleanField(
        verbose_name="İmtahanın statusu", default=False)
    exam_duration = models.IntegerField(verbose_name="İmtahan müddəti")

    def __str__(self):
        return self.name + " - " + self.variant

    def get_unique_slug(self):
        slug = slugify(self.name.
                       replace('ö', 'o').
                       replace('s', 'ş').
                       replace('u', 'ü').
                       replace('ı', 'i').
                       replace('ə', 'e')
                       )
        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "İmtahan növü"
        verbose_name_plural = "İmtahan növləri"


class Exam(models.Model):
    variant = models.CharField(max_length=1, verbose_name="Variant")
    exam_type = models.ForeignKey(
        ExamType, on_delete=models.CASCADE, verbose_name="İmtahan növü", related_name="exam_types", null=True, blank=True)
    exam_name = models.CharField(max_length=50, verbose_name="İmtahan adı")
    exam_name_slug = models.SlugField(
        max_length=50, verbose_name="İmtahan adı slug", null=True, blank=True)
    questions = models.ManyToManyField(
        ExamQuestion, verbose_name="İmtahan sualları", related_name="exam_questions", blank=True)
    listening = models.FileField(
        upload_to="listenings/", verbose_name="Listening", null=True, blank=True)
    reading = RichTextField(verbose_name="Reading", null=True, blank=True)

    def __str__(self):
        return f'{self.exam_name} - {self.variant}'

    def get_unique_slug(self):
        slug = slugify(self.exam_name.
                       replace('ö', 'o').
                       replace('s', 'ş').
                       replace('u', 'ü').
                       replace('ı', 'i').
                       replace('ə', 'e')
                       )
        return slug

    def save(self, *args, **kwargs):
        self.exam_name_slug = self.get_unique_slug()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "İmtahan"
        verbose_name_plural = "İmtahanlar"


class StudentExam(models.Model):
    exam = models.ForeignKey(
        ExamType, on_delete=models.CASCADE, verbose_name="İmtahan")
    student = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Tələbə")
    exam_date = models.DateField(
        verbose_name="Tələbənin seçdiyi imtahan tarixi", null=True, blank=True)
    exam_time = models.TimeField(
        verbose_name="Tələbənin seçdiyi imtahan vaxtı", null=True, blank=True)
    is_finished = models.BooleanField(
        verbose_name="İmtahan bitib", default=False)

    def __str__(self):
        return f'{self.student} - {self.exam}'

    def get_exam_datetime(self):
        return f'{self.exam_date} - {self.exam_time}'
    get_exam_datetime.short_description = "İmtahan tarixi və vaxtı"

    class Meta:
        verbose_name = "Tələbənin İmtahan Qeydiyyatı"
        verbose_name_plural = "Tələbənin İmtahan Qeydiyyatları"


class StudentAnswer(models.Model):
    student = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Tələbə")
    question = models.ForeignKey(
        ExamQuestion, on_delete=models.CASCADE, verbose_name="Sual")
    selected_variant = models.CharField(
        max_length=1, choices=QuestionAnswer.variants, verbose_name="Tələbənin cavabı", null=True, blank=True)
    given_answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} - {self.question.get_exam()} - {self.question} - {self.selected_variant}'

    class Meta:
        verbose_name = "Tələbənin Cavabı"
        verbose_name_plural = "Tələbənin Cavabları"


class ExamResult(models.Model):
    student_exam = models.ForeignKey(
        StudentExam, on_delete=models.CASCADE, verbose_name="Tələbənin İmtahanı")
    student_answers = models.ManyToManyField(
        StudentAnswer, verbose_name="Tələbənin Cavabları", blank=True, related_name="student_answers")
    exam_answers = models.ManyToManyField(
        QuestionAnswer, verbose_name="İmtahanın Cavabları", blank=True, related_name="exam_answers")
    result = models.PositiveIntegerField(verbose_name="Nəticə", default=0)
    right_answers = models.PositiveIntegerField(
        verbose_name="Düzgün cavabların sayı", default=0)
    wrong_answers = models.PositiveIntegerField(
        verbose_name="Səhv cavabların sayı", default=0)

    def __str__(self):
        return f'{self.student_exam.exam} - {self.student_exam.student} - {self.result}'

    class Meta:
        verbose_name = "İmtahan nəticəsi"
        verbose_name_plural = "İmtahan nəticələri"
