from django.contrib import admin, messages
from core.models import (
    SettingsModel, BannerModel, ContactInformationModel,
    SocialMediaModel, NewsModel, VideoGalleryModel,
    PhotoGalleryModel, PhotoGalleryItem, TeacherModel, ServiceModel,
    BranchModel, BranchContactNumberModel, SuccessModel,
    SuccessItemModel, ResumeModel, ContactModel, 
    AbiturientOnlineRegister, MasterOnlineRegister, MIQOnlineRegister,
    CivilServiceOnlineRegister, ComputerCourseOnlineRegister, AccountingOnlineRegister,
    ForeignLanguageOnlineRegister, HighSchoolOnlineRegister, PreSchoolOnlineRegister,
    PrimarySchoolOnlineRegister, EditionModel
)
from django.contrib.admin.sites import AdminSite

AdminSite.site_header = 'Panda School administrasiyası'
AdminSite.site_title = 'Panda School sayt administratoru'

@admin.register(SettingsModel)
class SettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("LOQO", {'fields': ('logo', 'logo_active')}),
        ("FAVICON", {'fields': ('favicon', 'favicon_active')}),
        ("ABOUT US", {'fields': ('about_us', 'about_active')}),
        ("SƏHİFƏ BANNERLƏRİ", {
            'fields': ('about_page_banner', 'success_page_banner', 
            'service_page_banner', 'news_page_banner',
            'gallery_page_banner', 'resume_page_banner', 
            'contact_page_banner', 'edition_page_banner', 
            'register_page_banner')
            }
        ),
        ("SƏHİFƏ AKTİVLİYİ", {
            'fields': ('about_page_active', 'success_page_active', 
            'service_page_active', 'news_page_active',
            'gallery_page_active', 'resume_page_active', 
            'contact_page_active', 'edition_page_active', 
            'register_page_active')
            }
        ),
        ("MESAJLAR", {
            'fields': ('student_message1', 'student_message2', 'student_message3')
            }
        ),   
    )

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

class PhotoGalleryItemAdmin(admin.TabularInline):
    model = PhotoGalleryItem
    extra = 3
    show_change_link = True

@admin.register(PhotoGalleryModel)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")
    inlines = [PhotoGalleryItemAdmin]

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

class BranchContactNumberAdmin(admin.TabularInline):
    model = BranchContactNumberModel
    extra = 3
    show_change_link = True

@admin.register(BranchModel)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")
    inlines = [BranchContactNumberAdmin]

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)


class SuccessItemAdmin(admin.TabularInline):
    model = SuccessItemModel
    extra = 3
    show_change_link = True

@admin.register(SuccessModel)
class SuccessAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")
    inlines = [SuccessItemAdmin]

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("ŞƏXSİ MƏLUMATLAR", {
            'fields': ('vacancy_name', 'full_name', 'email', 'birthdate',
            'subject', 'home_phone', 'mobile_phone', 'address')
            }
        ),
        ("İŞ TƏCRÜBƏSİ 1", {
            'fields': ('work_start_end_time1', 'company_name1', 'duty1', 'leaving_reason1')
            }
        ),
        ("İŞ TƏCRÜBƏSİ 2", {
            'fields': ('work_start_end_time2', 'company_name2', 'duty2', 'leaving_reason2')
            }
        ), 
        ("İŞ TƏCRÜBƏSİ 3", {
            'fields': ('work_start_end_time3', 'company_name3', 'duty3', 'leaving_reason3')
            }
        ),  
        ("TƏHSİL 1", {
            'fields': ('ed_start_end_time1', 'university1', 'speciality1', 'result1')
            }
        ),
        ("TƏHSİL 2", {
            'fields': ('ed_start_end_time2', 'university2', 'speciality2', 'result2')
            }
        ),
        ("TƏHSİL 3", {
            'fields': ('ed_start_end_time3', 'university3', 'speciality3', 'result3')
            }
        ),
        ("SERTIFIKATLAR, TƏLİMLƏR VƏ SEMİNARLAR 1", {
            'fields': ('ce_start_end_time1', 'qualification1', 'place1', 'success1')
            }
        ),
        ("SERTIFIKATLAR, TƏLİMLƏR VƏ SEMİNARLAR 2", {
            'fields': ('ce_start_end_time2', 'qualification2', 'place2', 'success2')
            }
        ),
        ("SERTIFIKATLAR, TƏLİMLƏR VƏ SEMİNARLAR 3", {
            'fields': ('ce_start_end_time3', 'qualification3', 'place3', 'success3')
            }
        ),
        ("DİGƏR NAİLİYYƏTLƏR", {
            'fields': ("other_successes",)
            }
        ),
        ("TÖVSİYƏ EDİLƏN ŞƏXSLƏR 1", {
            'fields': ('reference_full_name1', 'phone_number1', 'relation1')
            }
        ),
        ("TÖVSİYƏ EDİLƏN ŞƏXSLƏR 2", {
            'fields': ('reference_full_name2', 'phone_number2', 'relation2')
            }
        ),
    )
    readonly_fields = (
        "vacancy_name", "full_name", "email", "birthdate",
        "subject", "home_phone", "mobile_phone", "address",

        "work_start_end_time1", "company_name1", "duty1", "leaving_reason1",
        "work_start_end_time2", "company_name2", "duty2", "leaving_reason2",
        "work_start_end_time3", "company_name3", "duty3", "leaving_reason3",

        "ed_start_end_time1", "university1", "speciality1", "result1",
        "ed_start_end_time2", "university2", "speciality2", "result2",
        "ed_start_end_time3", "university3", "speciality3", "result3",

        "ce_start_end_time1", "qualification1", "place1", "success1",
        "ce_start_end_time2", "qualification2", "place2", "success2",
        "ce_start_end_time3", "qualification3", "place3", "success3",

        "other_successes",

        "reference_full_name1", "phone_number1", "relation1",
        "reference_full_name2", "phone_number2", "relation2",
    )
    list_display = ("full_name", "vacancy_name")

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "email", "subject", "message")

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(AbiturientOnlineRegister)
class AbiturientOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number", "school",
    "identity_card_number", "group", "student_class", "dim_point", "section")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(MasterOnlineRegister)
class MasterOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number",
    "university", "speciality", "identity_card_number", "dim_point", "language")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(MIQOnlineRegister)
class MIQOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number",
    "university", "speciality", "identity_card_number")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(CivilServiceOnlineRegister)
class CivilServiceOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number",
    "university", "identity_card_number")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(ForeignLanguageOnlineRegister)
class ForeignLanguageOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number",
    "identity_card_number", "language")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(ComputerCourseOnlineRegister)
class ComputerCourseOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number", "identity_card_number", "program_type")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(AccountingOnlineRegister)
class AccountingOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number",
    "identity_card_number")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(HighSchoolOnlineRegister)
class HighSchoolOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number", "identity_card_number", "student_class")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(PreSchoolOnlineRegister)
class PreSchoolOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number",
    "identity_card_number")

    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(PrimarySchoolOnlineRegister)
class PrimarySchoolOnlineRegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name", "email", "mobile_number",
    "identity_card_number")

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(ContactInformationModel)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(SocialMediaModel)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(VideoGalleryModel)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)

@admin.register(EditionModel)
class EditionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")

    actions = ['get_activated', 'get_deactivated']

    @admin.action(description="Aktiv et")
    def get_activated(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, "Seçilmiş elementlər aktivləşdirildi.", messages.SUCCESS)

    @admin.action(description="Deaktiv et")
    def get_deactivated(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, "Seçilmiş elementlər deaktivləşdirildi.", messages.SUCCESS)


# def get_app_list(self, request, app_label=None):
#         app_dict = self._build_app_dict(request)
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

#         for app in app_list:
#             if app['app_label'] == 'prestij':
#                 ordering = {
#                     "Parametrlər": 1,
#                     "Bannerlər": 2,
#                     "Sosial media hesabları": 3,
#                     "Əlaqə məlumatları": 4,
#                     "Müəllimlər": 5,
#                     "Filiallar": 6,
#                     "Uğurlar": 7,
#                     "Xidmətlər": 8,
#                     "Xəbərlər": 9,
#                     "Foto Qalereya": 10,
#                     "Video Qalereya": 11,
#                     "Nəşrlərimiz": 12,
#                     "CVlər": 13,
#                     "Mesajlar": 14,
#                     "Müəllim qeydiyyatlar": 15,
#                     "Abituriyent qeydiyyatlar": 16,
#                     "Master qeydiyyatlar": 17,
#                     "MIQ qeydiyyatlar": 18,
#                     "Dövlət qulluğu qeydiyyatlar": 19,
#                     "Kompüter kursu qeydiyyatlar": 20,
#                     "Xarici dillər qeydiyyatlar": 21,
#                     "Mühasibatlıq qeydiyyatlar": 22,
#                     "Liseylərə hazırlıq qeydiyyatlar": 23,
#                     "Məktəbəqədər hazırlıq qeydiyyatlar": 24,
#                     "İbtidai qeydiyyatlar": 25,
#                 }
#                 app['models'].sort(key=lambda x: ordering[x['name']])

#             if app['app_label'] == 'auth':
#                 ordering = {
#                     "Istifadəçilər" : 1,
#                 }
#                 app['models'].sort(key=lambda x: ordering[x['name']])

#         return app_list

# admin.AdminSite.get_app_list = get_app_list
# mysite = MyAdminSite()
# admin.site = mysite
# admin.sites.site = mysite