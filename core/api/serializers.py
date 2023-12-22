from rest_framework import serializers
from core.models import (
    SettingsModel, BannerModel, ContactInformationModel,
    SocialMediaModel, NewsModel, VideoGalleryModel,
    PhotoGalleryModel, PhotoGalleryItem, TeacherModel, ServiceModel,
    BranchModel, BranchContactNumberModel, SuccessModel,
    SuccessItemModel, ResumeModel, ContactModel, TeacherOnlineRegister,
    AbiturientOnlineRegister, MasterOnlineRegister, MIQOnlineRegister,
    CivilServiceOnlineRegister, ComputerCourseOnlineRegister, ForeignLanguageOnlineRegister,
    AccountingOnlineRegister, HighSchoolOnlineRegister, PreSchoolOnlineRegister,
    PrimarySchoolOnlineRegister, EditionModel,
)


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = "__all__"


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformationModel
        fields = "__all__"


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaModel
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = "__all__"


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGalleryModel
        fields = "__all__"


class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGalleryModel
        fields = "__all__"


class PhotoGalleryItemSerializer(serializers.ModelSerializer):
    photo_gallery = PhotoGallerySerializer()

    class Meta:
        model = PhotoGalleryItem
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = "__all__"


class BranchContactNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = BranchContactNumberModel
        fields = ['phone_number']


class BranchSerializer(serializers.ModelSerializer):
    contact_numbers = BranchContactNumberSerializer(many=True)

    class Meta:
        model = BranchModel
        fields = ['id', 'name', 'website', 'email', 'address',
                  'map_url', 'is_active', 'contact_numbers']


class SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessModel
        fields = "__all__"


class SuccessItemSerializer(serializers.ModelSerializer):
    success = SuccessSerializer()

    class Meta:
        model = SuccessItemModel
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeModel
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"


class TeacherOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherOnlineRegister
        fields = "__all__"


class AbiturientOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbiturientOnlineRegister
        fields = "__all__"


class MasterOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterOnlineRegister
        fields = "__all__"


class MIQOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MIQOnlineRegister
        fields = "__all__"


class CivilServiceOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CivilServiceOnlineRegister
        fields = "__all__"


class ComputerCourseOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerCourseOnlineRegister
        fields = "__all__"


class ForeignLanguageOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignLanguageOnlineRegister
        fields = "__all__"


class AccountingOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingOnlineRegister
        fields = "__all__"


class HighSchoolOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchoolOnlineRegister
        fields = "__all__"


class PreSchoolOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreSchoolOnlineRegister
        fields = "__all__"


class PrimarySchoolOnlineRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimarySchoolOnlineRegister
        fields = "__all__"


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditionModel
        fields = "__all__"
