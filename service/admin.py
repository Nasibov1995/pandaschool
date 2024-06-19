from django.contrib import admin
from django.http.request import HttpRequest
from service.models import (
    BranchModel, SeasonModel, StudentCategoryModel, StudentModel, TeacherModel,
    BlockModel, SubjectModel, ClassModel, GroupModel, LanguageModel,
    TeacherPaymentInformationModel, StudentPaymentInformationModel, MonthModel
)
import csv
from django.http import HttpResponse

from django.contrib import messages
from notification.models import NotificationModel

admin.site.register(BranchModel)

@admin.register(SeasonModel)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("__str__", "branch", "start_date", "end_date")

    def get_queryset(self, request):
        qs = super(SeasonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(branch__branch_accountant__account=request.user)

    def delete_queryset(self, request, queryset):
        content = str(queryset.count()) + " sezon silindi: "
        for query in queryset:
            content += query.name + " " + query.branch.name + " filialı, "
        NotificationModel.objects.create(
            content = content,
            type = "D"
        )
        return super().delete_queryset(request, queryset)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'branch' and not request.user.is_superuser:
            kwargs["queryset"] = BranchModel.objects.filter(branch_accountant__account = request.user)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(StudentCategoryModel)
admin.site.register(BlockModel)
admin.site.register(SubjectModel)
admin.site.register(ClassModel)
admin.site.register(GroupModel)
admin.site.register(LanguageModel)

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "season", "status")
    list_filter = ("status",)
    search_fields = ("first_name", "last_name")

    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(season__branch__branch_accountant__account=request.user)

    def delete_queryset(self, request, queryset):
        content = str(queryset.count()) + " tələbə silindi: "
        for query in queryset:
            content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
        NotificationModel.objects.create(
            content = content,
            type = "D"
        )
        return super().delete_queryset(request, queryset)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'season' and not request.user.is_superuser:
            kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    actions = ("mark_as_de", "mark_as_d", "mark_as_b")

    @admin.action(description="Seçilmiş Tələbələri davam edir kimi göstər")
    def mark_as_de(self, request, queryset):
        updated = queryset.update(status="DE")
        self.message_user(request, "Seçilmiş Tələbələr davam edir.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Tələbələri dondurulub kimi göstər")
    def mark_as_d(self, request, queryset):
        updated = queryset.update(status="D")
        self.message_user(request, "Seçilmiş Tələbələr dondurulub.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Tələbələri bitirilib kimi göstər")
    def mark_as_b(self, request, queryset):
        updated = queryset.update(status="B")
        self.message_user(request, "Seçilmiş Tələbələr bitirilib.", messages.SUCCESS)

class TeacherPaymentInformationAdmin(admin.TabularInline):
    model = TeacherPaymentInformationModel
    extra = 0

@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("__str__", "specialty", "section", "salary", "status")
    list_filter = ("status",)
    search_fields = ("first_name", "last_name")

    inlines = [TeacherPaymentInformationAdmin]

    def get_queryset(self, request):
        qs = super(TeacherAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(season__branch__branch_accountant__account=request.user)

    def delete_queryset(self, request, queryset):
        content = str(queryset.count()) + " müəllim silindi: "
        for query in queryset:
            content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
        NotificationModel.objects.create(
            content = content,
            type = "D"
        )
        return super().delete_queryset(request, queryset)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'season' and not request.user.is_superuser:
            kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    actions = ("mark_as_qe", "mark_as_ts", "mark_as_fm")

    @admin.action(description="Seçilmiş Müəllimləri qeyd edilməyib kimi göstər")
    def mark_as_qe(self, request, queryset):
        updated = queryset.update(status="QE")
        self.message_user(request, "Seçilmiş Müəllimlər qeyd edilməyib.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Müəllimləri tələbə sayı kimi göstər")
    def mark_as_ts(self, request, queryset):
        updated = queryset.update(status="TS")
        self.message_user(request, "Seçilmiş Müəllimlər tələbə sayına görə maaş alır.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Müəllimləri fiks maaş kimi göstər")
    def mark_as_fm(self, request, queryset):
        updated = queryset.update(status="FM")
        self.message_user(request, "Seçilmiş Müəllimlər fiks maaş alır.", messages.SUCCESS)



@admin.register(MonthModel)
class MonthAdmin(admin.ModelAdmin):
    list_display = ("__str__", "season")
    
admin.site.register(StudentPaymentInformationModel)
@admin.register(TeacherPaymentInformationModel)
class TeacherPaymentInformationAdmin(admin.ModelAdmin):
    list_display = ("teacher", "month", "payment_date", "payment_amount", "status")
    list_filter = ("status", "payment_date")
    search_fields = ("teacher__first_name", "teacher__last_name")
    show_full_result_count = False

    actions = ("mark_as_true", "mark_as_false", "export_as_csv")

    @admin.action(description="Seçilmiş Müəllimlər ödəniş aldı.")
    def mark_as_true(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş Müəllimlər ödəniş aldı.", messages.SUCCESS)

    @admin.action(description="Seçilmiş Müəllimlər ödəniş almayıb.")
    def mark_as_false(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş Müəllimlər ödəniş almayıb.", messages.SUCCESS)

    @admin.action(description="CSV kimi ixrac edin")
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response




# admin.site.register(AbiturientBlockModel)
# admin.site.register(AbiturientClassModel)
# admin.site.register(AbiturientSubjectModel)
# admin.site.register(AbiturientGroupModel)

# class AbiturientPaymentInformationAdmin(admin.TabularInline):
#     model = AbiturientPaymentInformationModel
#     extra = 0

# @admin.register(AbiturientModel)
# class AbiturientAdmin(admin.ModelAdmin):
#     list_display = ("__str__", "sector", "dim_point")
#     list_filter = ("sector", )
#     filter_horizontal = ('subjects', 'blocks')

#     inlines = [AbiturientPaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(AbiturientAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " abiturient silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 
#     actions = ("mark_as_az", "mark_as_ru")

#     @admin.action(description="Seçilmiş Abituriyentlər azərbaycan dili bölməsi et")
#     def mark_as_az(self, request, queryset):
#         updated = queryset.update(sector="AZ")
#         self.message_user(request, "Seçilmiş Abituriyentlər azərbaycan dili bölməsi edildi.", messages.SUCCESS)

#     @admin.action(description="Seçilmiş Abituriyentlər rus dili bölməsi et")
#     def mark_as_ru(self, request, queryset):
#         updated = queryset.update(sector="RU")
#         self.message_user(request, "Seçilmiş Abituriyentlər rus dili bölməsi edildi.", messages.SUCCESS)



# admin.site.register(MasterForeignLanguageModel)
# admin.site.register(MasterSubjectModel)
# admin.site.register(MasterGroupModel)

# class MasterPaymentInformationAdmin(admin.TabularInline):
#     model = MasterPaymentInformationModel
#     extra = 0

# @admin.register(MasterModel)
# class MasterAdmin(admin.ModelAdmin):
#     list_display = ("__str__", "dim_point")
#     filter_horizontal = ("subjects",)
#     inlines = [MasterPaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(MasterAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " magistraturaya hazırlıq tələbəsi silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 

# admin.site.register(MIQSubjectModel)

# class MIQPaymentInformationAdmin(admin.TabularInline):
#     model = MIQPaymentInformationModel
#     extra = 0

# @admin.register(MIQModel)
# class MIQAdmin(admin.ModelAdmin):
#     list_display = ("__str__", "specialty")
#     filter_horizontal = ("subjects",)
#     inlines = [MIQPaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(MIQAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " miq tələbəsi silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 

# admin.site.register(CivilServiceSubjectModel)

# class CivilServicePaymentInformationAdmin(admin.TabularInline):
#     model = CivilServicePaymentInformationModel
#     extra = 0


# @admin.register(CivilServiceModel)
# class CivilServiceAdmin(admin.ModelAdmin):
#     filter_horizontal = ("subjects",)
#     inlines = [CivilServicePaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(CivilServiceAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " dövlət qulluğu tələbəsi silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 

# class ForeignLanguagePaymentInformationAdmin(admin.TabularInline):
#     model = ForeignLanguagePaymentInformationModel
#     extra = 0

# @admin.register(ForeignLanguageModel)
# class ForeignLanguageAdmin(admin.ModelAdmin):
#     inlines = [ForeignLanguagePaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(ForeignLanguageAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " xarici dil tələbəsi silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 


# admin.site.register(ComputerProgramTypeModel)

# class ComputerCoursePaymentInformationAdmin(admin.TabularInline):
#     model = ComputerCoursePaymentInformationModel
#     extra = 0

# @admin.register(ComputerCourseModel)
# class ComputerCourseAdmin(admin.ModelAdmin):
#     filter_horizontal = ("program_types",)
#     inlines = [ComputerCoursePaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(ComputerCourseAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " kompüter kurs tələbəsi silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 

# class AccountingPaymentInformationAdmin(admin.TabularInline):
#     model = AccountingPaymentInformationModel
#     extra = 0

# @admin.register(AccountingModel)
# class AccountingAdmin(admin.ModelAdmin):
#     inlines = [AccountingPaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(AccountingAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " mühasibatlıq tələbəsi silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 


# admin.site.register(HighSchoolClassModel)
# admin.site.register(HighSchoolSubjectModel)
# admin.site.register(HighSchoolGroupModel)

# class HighSchoolPaymentInformationAdmin(admin.TabularInline):
#     model = HighSchoolPaymentInformationModel
#     extra = 0

# @admin.register(HighSchoolModel)
# class HighSchoolAdmin(admin.ModelAdmin):
#     filter_horizontal = ("subjects",)
#     inlines = [HighSchoolPaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(HighSchoolAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " liseylərə hazırlıq tələbəsi silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 

# admin.site.register(PreSchoolSubjectModel)

# class PreSchoolPaymentInformationAdmin(admin.TabularInline):
#     model = PreSchoolPaymentInformationModel
#     extra = 0

# @admin.register(PreSchoolModel)
# class PreSchoolAdmin(admin.ModelAdmin):
#     filter_horizontal = ("subjects", )
#     inlines = [PreSchoolPaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(PreSchoolAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " məktəbəqədər hazırlıq silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 

# admin.site.register(PrimarySchoolClassModel)
# admin.site.register(PrimarySchoolSubjectModel)
# admin.site.register(PrimarySchoolGroupModel)

# class PrimarySchoolPaymentInformationAdmin(admin.TabularInline):
#     model = PrimarySchoolPaymentInformationModel
#     extra = 0

# @admin.register(PrimarySchoolModel)
# class PrimarySchoolAdmin(admin.ModelAdmin):
#     filter_horizontal = ("subjects",)
#     inlines = [PrimarySchoolPaymentInformationAdmin]

#     def get_queryset(self, request):
#         qs = super(PrimarySchoolAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(season__branch__branch_accountant__account=request.user)

#     def delete_queryset(self, request, queryset):
#         content = str(queryset.count()) + " ibtidai silindi: "
#         for query in queryset:
#             content += query.season.branch.name + " filialı - " + query.first_name + " " + query.last_name + ", "
#         NotificationModel.objects.create(
#             content = content,
#             type = "D"
#         )
#         return super().delete_queryset(request, queryset)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'season' and not request.user.is_superuser:
#             kwargs["queryset"] = SeasonModel.objects.filter(branch__branch_accountant__account = request.user)
#             return super().formfield_for_foreignkey(db_field, request, **kwargs)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
 
