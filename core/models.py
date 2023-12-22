from django.db import models
from ckeditor.fields import RichTextField

class SettingsModel(models.Model):
    logo = models.ImageField("Loqo", upload_to="logo/", blank=True, null=True)
    logo_active = models.BooleanField("Status", default=True)
    favicon = models.ImageField("Ikon", upload_to="favicon/", blank=True, null=True)
    favicon_active = models.BooleanField("Status", default=True)
    about_us = RichTextField("Haqqımızda", blank=True, null=True)
    about_active = models.BooleanField("Status", default=True)

    about_page_banner = models.ImageField("Haqqımızda", upload_to="banner_images/", blank=True, null=True)
    about_page_active = models.BooleanField("Haqqımızda", default=True)
    success_page_banner = models.ImageField("Uğurlarımız", upload_to="banner_images/", blank=True, null=True)
    success_page_active = models.BooleanField("Uğurlarımız", default=True)
    service_page_banner = models.ImageField("Xidmətlərimiz", upload_to="banner_images/", blank=True, null=True)
    service_page_active = models.BooleanField("Xidmətlərimiz", default=True)
    news_page_banner = models.ImageField("Xəbərlər", upload_to="banner_images/", blank=True, null=True)
    news_page_active = models.BooleanField("Xəbərlər", default=True)
    gallery_page_banner = models.ImageField("Foto Qalereya", upload_to="banner_images/", blank=True, null=True)
    gallery_page_active = models.BooleanField("Foto Qalereya", default=True)
    video_gallery_page_banner = models.ImageField("Video Qalereya", upload_to="banner_images/", blank=True, null=True)
    video_gallery_page_active = models.BooleanField("Video Qalereya", default=True)
    resume_page_banner = models.ImageField("CV göndər", upload_to="banner_images/", blank=True, null=True)
    resume_page_active = models.BooleanField("CV göndər", default=True)
    contact_page_banner = models.ImageField("Əlaqə", upload_to="banner_images/", blank=True, null=True)
    contact_page_active = models.BooleanField("Əlaqə", default=True)
    edition_page_banner = models.ImageField("Nəşrlərimiz", upload_to="banner_images/", blank=True, null=True)
    edition_page_active = models.BooleanField("Nəşrlərimiz", default=True)
    register_page_banner = models.ImageField("Kursa onlayn qeydiyyat", upload_to="banner_images/", blank=True, null=True)
    register_page_active = models.BooleanField("Kursa onlayn qeydiyyat", default=True)

    student_message1 = models.TextField("Ödəniş tarixinə 3 gün qalmış mesaj", blank=True, null=True)
    student_message2 = models.TextField("Ödəniş tarixində mesaj", blank=True, null=True)
    student_message3 = models.TextField("Ödəniş tarixindən 3 gün sonra mesaj", blank=True, null=True)

    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametrlər"

    def __str__(self):
        return "Parametrlər"

class BannerModel(models.Model):
    image = models.ImageField("Şəkil", upload_to="banner_images/")
    title = models.CharField("Başlıq", max_length=256, blank=True, null=True)
    link = models.URLField("Link", max_length=2048, blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlər"

    def __str__(self):
        return self.title

class ContactInformationModel(models.Model):
    email = models.EmailField("Email", max_length=256, blank=True, null=True)
    contact_number = models.CharField("Əlaqə nömrəsi", max_length=256, blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Əlaqə məlumatı"
        verbose_name_plural = "Əlaqə məlumatları"
        ordering = ("-id", )

    def __str__(self):
        contact_informations = ContactInformationModel.objects.all()
        return "Əlaqə məlumatı " + str(list(contact_informations).index(self) + 1)

class SocialMediaModel(models.Model):
    name = models.CharField("Ad", max_length=100)
    icon_name = models.TextField("İkon")
    color_code = models.TextField("Rəng kodu", blank=True, null=True)
    link = models.URLField("Link", max_length=2048, blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Sosial media"
        verbose_name_plural = "Sosial media hesabları"
        ordering = ("-id", )

    def __str__(self):
        return self.name

class NewsModel(models.Model):
    title = models.CharField("Başlıq", max_length=256)
    image = models.ImageField("Şəkil", upload_to="news_images/", blank=True, null=True)
    pub_date = models.DateField("Tarix", blank=True, null=True)
    content = RichTextField("Məzmun", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"
        ordering = ("-id", )

    def __str__(self):
        return self.title

class VideoGalleryModel(models.Model):
    video_link = models.URLField("Video linki", max_length=2048)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Video Qalereya"
        ordering = ("-id", )

    def save(self, *args, **kwargs):
        if "watch?v=" in self.video_link:
            self.video_link = self.video_link.replace("watch?v=", "embed/")
        super(VideoGalleryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.video_link[:150] + "..."

class PhotoGalleryModel(models.Model):
    title = models.TextField("Başlıq", max_length=528)
    image = models.ImageField("Şəkil", upload_to="photo_gallery_images/")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Foto Qalereya"
        verbose_name_plural = "Foto Qalereya"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class PhotoGalleryItem(models.Model):
    title = models.TextField("Başlıq", max_length=528)
    image = models.ImageField("Şəkil", upload_to="photo_gallery_item_images/")
    photo_gallery = models.ForeignKey(PhotoGalleryModel, on_delete=models.CASCADE, related_name="photo_gallery_items")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotolar"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class TeacherModel(models.Model):
    name = models.CharField("Ad", max_length=100)
    image = models.ImageField("Şəkil", upload_to="teacher_images/", blank=True, null=True)
    surname = models.CharField("Soyad", max_length=100)
    profession = models.TextField("Sahə", blank=True, null=True)
    mission = models.TextField("Vəzifə", blank=True, null=True)
    about = models.TextField("Haqqında", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Müəllim"
        verbose_name_plural = "Müəllimlər"
        ordering = ("-id", )

    def __str__(self):
        return self.name + " " + self.surname

class ServiceModel(models.Model):
    title = models.CharField("Başlıq", max_length=256)
    image = models.ImageField("Şəkil", upload_to="service_images/")
    content = RichTextField("Məzmun", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class BranchModel(models.Model):
    name = models.CharField("Ad", max_length=256)
    website = models.URLField("Vebsayt", max_length=2048, blank=True, null=True)
    email = models.EmailField("Email", max_length=256, blank=True, null=True)
    address = models.TextField("Ünvan", blank=True, null=True)
    map_url = models.URLField("Xəritə linki", max_length=2048, blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class BranchContactNumberModel(models.Model):
    phone_number = models.CharField("Əlaqə nömrəsi", max_length=50)
    branch = models.ForeignKey(BranchModel, on_delete=models.CASCADE, related_name="contact_numbers")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Filial əlaqə nömrəsi"
        verbose_name_plural = "Filial əlaqə nömrələri"
        ordering = ("-id",)

    def __str__(self):
        return self.phone_number

class SuccessModel(models.Model):
    title = models.TextField("Başlıq")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Uğur"
        verbose_name_plural = "Uğurlar"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class SuccessItemModel(models.Model):
    name = models.CharField("Ad soyad", max_length=128, blank=True, null=True)
    image = models.ImageField("Şəkil", upload_to="success_images/", blank=True, null=True)
    item = models.TextField("Məzmun")
    success = models.ForeignKey(SuccessModel, on_delete=models.CASCADE, related_name="success_items")
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Uğur məzmunu"
        verbose_name_plural = "Uğur məzmunları"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class ResumeModel(models.Model):
    # personal info
    vacancy_name = models.TextField("Müraciət edilən vakansiyanın adı")
    full_name = models.TextField("Soyad, ad, ata adı")
    email = models.EmailField("Email")
    birthdate = models.TextField("Doğum tarixi")
    subject = models.TextField("Tədris etmək istənilən fənn")
    home_phone = models.TextField("Ev telefon nömrəsi")
    mobile_phone = models.TextField("Mobil nömrə")
    address = models.TextField("Ünvan")
    

    # work experience
    work_start_end_time1 = models.TextField("İşlədiyi başlanğıc və son tarixlər 1", blank=True, null=True)
    company_name1 = models.TextField("Şirkətin adı, ünvanı və fəaliyyət göstərdiyi sahə 1", blank=True, null=True)
    duty1 = models.TextField("Vəzifə və əsas öhdəliklər 1", blank=True, null=True)
    leaving_reason1 = models.TextField("Tərk etmə səbəbi 1", blank=True, null=True)

    work_start_end_time2 = models.TextField("İşlədiyi başlanğıc və son tarixlər 2", blank=True, null=True)
    company_name2 = models.TextField("Şirkətin adı, ünvanı və fəaliyyət göstərdiyi sahə 2", blank=True, null=True)
    duty2 = models.TextField("Vəzifə və əsas öhdəliklər 2", blank=True, null=True)
    leaving_reason2 = models.TextField("Tərk etmə səbəbi 2", blank=True, null=True)

    work_start_end_time3 = models.TextField("İşlədiyi başlanğıc və son tarixlər 3", blank=True, null=True)
    company_name3 = models.TextField("Şirkətin adı, ünvanı və fəaliyyət göstərdiyi sahə 3", blank=True, null=True)
    duty3 = models.TextField("Vəzifə və əsas öhdəliklər 3", blank=True, null=True)
    leaving_reason3 = models.TextField("Tərk etmə səbəbi 3", blank=True, null=True)

    # education
    ed_start_end_time1 = models.TextField("Təhsil aldığı başlanğıc və son tarix 1", blank=True, null=True)
    university1 = models.TextField("Universitet 1", blank=True, null=True)
    speciality1 = models.TextField("İxtisas və dərəcə 1", blank=True, null=True)
    result1 = models.TextField("Nəticə/Qiymət ortalaması 1", blank=True, null=True)

    ed_start_end_time2 = models.TextField("Təhsil aldığı başlanğıc və son tarix 2", blank=True, null=True)
    university2 = models.TextField("Universitet 2", blank=True, null=True)
    speciality2 = models.TextField("İxtisas və dərəcə 2", blank=True, null=True)
    result2 = models.TextField("Nəticə/Qiymət ortalaması 2", blank=True, null=True)

    ed_start_end_time3 = models.TextField("Təhsil aldığı başlanğıc və son tarix 3", blank=True, null=True)
    university3 = models.TextField("Universitet 3", blank=True, null=True)
    speciality3 = models.TextField("İxtisas və dərəcə 3", blank=True, null=True)
    result3 = models.TextField("Nəticə/Qiymət ortalaması 3", blank=True, null=True)

    # certificates, trainings, seminars
    ce_start_end_time1 = models.TextField("İştirak tarixi: başlanğıc və son tarix 1", blank=True, null=True)
    qualification1 = models.TextField("Kvalifikasiya 1", blank=True, null=True)
    place1 = models.TextField("Keçirildiyi məkan 1", blank=True, null=True)
    success1 = models.TextField("Əldə etdiyi nailiyyət 1", blank=True, null=True)

    ce_start_end_time2 = models.TextField("İştirak tarixi: başlanğıc və son tarix 2", blank=True, null=True)
    qualification2 = models.TextField("Kvalifikasiya 2", blank=True, null=True)
    place2 = models.TextField("Keçirildiyi məkan 2", blank=True, null=True)
    success2 = models.TextField("Əldə etdiyi nailiyyət 2", blank=True, null=True)

    ce_start_end_time3 = models.TextField("İştirak tarixi: başlanğıc və son tarix 3", blank=True, null=True)
    qualification3 = models.TextField("Kvalifikasiya 3", blank=True, null=True)
    place3 = models.TextField("Keçirildiyi məkan 3", blank=True, null=True)
    success3 = models.TextField("Əldə etdiyi nailiyyət 3", blank=True, null=True)

    # other successes
    other_successes = models.TextField("Digər nailiyyətlər", blank=True, null=True)

    # references
    reference_full_name1 = models.TextField("Soyad, adı, ata adı 1", blank=True, null=True)
    phone_number1 = models.TextField("Mobil nömrə 1", blank=True, null=True)
    relation1 = models.TextField("Əlaqə 1", blank=True, null=True)

    reference_full_name2 = models.TextField("Soyad, adı, ata adı 2", blank=True, null=True)
    phone_number2 = models.TextField("Mobil nömrə 2", blank=True, null=True)
    relation2 = models.TextField("Əlaqə 2", blank=True, null=True)

    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CVlər"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name

class ContactModel(models.Model):
    name = models.CharField("Ad", max_length=100)
    email = models.EmailField("Email", max_length=256)
    subject = models.TextField("Mövzu")
    message = models.TextField("Mesaj")

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class TeacherOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    SECTORS = (
        ("AZ", "Azərbaycan dili"),
        ("RU", "Rus dili"),
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email")
    mobile_number = models.TextField("Mobil nömrə")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    speciality = models.TextField("İxtisas")
    section = models.CharField("Bölmə", max_length=2, choices=SECTORS, default="AZ")
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Müəllim qeydiyyat"
        verbose_name_plural = "Müəllim qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name


class AbiturientOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    SECTORS = (
        ("AZ", "Azərbaycan dili"),
        ("RU", "Rus dili"),
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    school = models.TextField("Təhsil aldığı məktəb")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    group = models.TextField("Qrup")
    student_class = models.IntegerField("Sinif")
    dim_point = models.FloatField("Dim balı")
    section = models.CharField("Bölmə", max_length=2, choices=SECTORS, default="AZ")
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Abituriyent qeydiyyat"
        verbose_name_plural = "Abituriyent qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name

class MasterOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    university = models.TextField("Bitirdiyi universitet")
    speciality = models.TextField("İxtisas")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    dim_point = models.FloatField("Qəbul balı")
    language = models.TextField("Xarici dil")
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "MIQ qeydiyyat"
        verbose_name_plural = "MIQ qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name

class MIQOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    university = models.TextField("Bitirdiyi universitet")
    speciality = models.TextField("İxtisas")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "MIQ qeydiyyat"
        verbose_name_plural = "MIQ qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
class CivilServiceOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    university = models.TextField("Bitirdiyi universitet")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Dövlət qulluğu qeydiyyat"
        verbose_name_plural = "Dövlət qulluğu qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
class ForeignLanguageOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    language = models.TextField("Xarici dil")
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Xarici dil qeydiyyat"
        verbose_name_plural = "Xarici dillər qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name

class ComputerCourseOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    program_type = models.TextField("Proqram növü")
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Kompüter kursu qeydiyyat"
        verbose_name_plural = "Kompüter kursu qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
class AccountingOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Mühasibatlıq qeydiyyat"
        verbose_name_plural = "Mühasibatlıq qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
class HighSchoolOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    student_class = models.IntegerField("Sinif")
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Liseylərə hazırlıq qeydiyyat"
        verbose_name_plural = "Liseylərə hazırlıq qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
class PreSchoolOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "Məktəbəqədər hazırlıq qeydiyyat"
        verbose_name_plural = "Məktəbəqədər hazırlıq qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
class PrimarySchoolOnlineRegister(models.Model):
    STATUS = (
        ("T", "Tamamlandı"),
        ("TM", "Tamamlanmadı")
    )
    full_name = models.TextField("Ad, soyad")
    email = models.EmailField("Email", max_length=256)
    mobile_number = models.TextField("Mobil nömrə")
    identity_card_number = models.TextField("Şəxsiyyət vəsiqəsinin nömrəsi", blank=True, null=True)
    student_class = models.IntegerField("Sinif")
    status = models.CharField("Status", choices=STATUS, max_length=2, default="TM")

    class Meta:
        verbose_name = "İbtidai qeydiyyat"
        verbose_name_plural = "İbtidai qeydiyyatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.full_name
    
class EditionModel(models.Model):
    title = models.TextField("Başlıq")
    image = models.ImageField("Şəkil", upload_to="edition_images/", blank=True, null=True)
    content = models.TextField("Məzmun", blank=True, null=True)
    is_active = models.BooleanField("Status", default=False)

    class Meta:
        verbose_name = "Nəşr"
        verbose_name_plural = "Nəşrlərimiz"
        ordering = ("-id",)

    def __str__(self):
        return self.title
