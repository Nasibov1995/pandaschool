from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
)
from core.models import (
    SettingsModel, BannerModel, ContactInformationModel,
    SocialMediaModel, NewsModel, VideoGalleryModel,
    PhotoGalleryModel, PhotoGalleryItem, TeacherModel, ServiceModel,
    BranchModel, BranchContactNumberModel, SuccessModel,
    SuccessItemModel, ResumeModel, ContactModel, TeacherOnlineRegister,
    AbiturientOnlineRegister, MasterOnlineRegister, MIQOnlineRegister,
    CivilServiceOnlineRegister, ComputerCourseOnlineRegister, ForeignLanguageOnlineRegister,
    AccountingOnlineRegister, HighSchoolOnlineRegister, PreSchoolOnlineRegister,
    PrimarySchoolOnlineRegister, EditionModel
)
from core.api.serializers import (
    SettingsSerializer, BannerSerializer, ContactInformationSerializer,
    SocialMediaSerializer, NewsSerializer, VideoGallerySerializer,
    PhotoGallerySerializer, PhotoGalleryItemSerializer, TeacherSerializer, ServiceSerializer,
    BranchSerializer, BranchContactNumberSerializer, SuccessSerializer,
    SuccessItemSerializer, ResumeSerializer, ContactSerializer, TeacherOnlineRegisterSerializer,
    AbiturientOnlineRegisterSerializer, MasterOnlineRegisterSerializer, MIQOnlineRegisterSerializer,
    CivilServiceOnlineRegisterSerializer, ComputerCourseOnlineRegisterSerializer, ForeignLanguageOnlineRegisterSerializer,
    AccountingOnlineRegisterSerializer, HighSchoolOnlineRegisterSerializer, PreSchoolOnlineRegisterSerializer,
    PrimarySchoolOnlineRegisterSerializer, EditionSerializer
)

class SettingsListAPIView(ListAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer

class BannerListAPIView(ListAPIView):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializer

class ContactInformationListAPIView(ListAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMediaModel.objects.all()
    serializer_class = SocialMediaSerializer

class NewsListAPIView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"

class VideoGalleryListAPIView(ListAPIView):
    queryset = VideoGalleryModel.objects.all()
    serializer_class = VideoGallerySerializer

class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGalleryModel.objects.all()
    serializer_class = PhotoGallerySerializer

class PhotoGalleryItemListAPIView(ListAPIView):
    queryset = PhotoGalleryItem.objects.all()
    serializer_class = PhotoGalleryItemSerializer

class TeacherListAPIView(ListAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveAPIView(RetrieveAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = "id"

class ServiceListAPIView(ListAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveAPIView(RetrieveAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "id"

class BranchListAPIView(ListAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer

class BranchContactNumberListAPIView(ListAPIView):
    queryset = BranchContactNumberModel.objects.all()
    serializer_class = BranchContactNumberSerializer

class SuccessListAPIView(ListAPIView):
    queryset = SuccessModel.objects.all()
    serializer_class = SuccessSerializer

class SuccessItemListAPIView(ListAPIView):
    queryset = SuccessItemModel.objects.all()
    serializer_class = SuccessItemSerializer

class ResumeCreateAPIView(CreateAPIView):
    queryset = ResumeModel.objects.all()
    serializer_class = ResumeSerializer

class ContactCreateAPIView(CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

class TeacherOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = TeacherOnlineRegister.objects.all()
    serializer_class = TeacherOnlineRegisterSerializer

class AbiturientOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = AbiturientOnlineRegister.objects.all()
    serializer_class = AbiturientOnlineRegisterSerializer

class MasterOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = MasterOnlineRegister.objects.all()
    serializer_class = MasterOnlineRegisterSerializer

class MIQOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = MIQOnlineRegister.objects.all()
    serializer_class = MIQOnlineRegisterSerializer

class CivilServiceOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = CivilServiceOnlineRegister.objects.all()
    serializer_class = CivilServiceOnlineRegisterSerializer

class ComputerCourseOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = ComputerCourseOnlineRegister.objects.all()
    serializer_class = ComputerCourseOnlineRegisterSerializer

class ForeignLanguageOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = ForeignLanguageOnlineRegister.objects.all()
    serializer_class = ForeignLanguageOnlineRegisterSerializer

class AccountingOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = AccountingOnlineRegister.objects.all()
    serializer_class = AccountingOnlineRegisterSerializer

class HighSchoolOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = HighSchoolOnlineRegister.objects.all()
    serializer_class = HighSchoolOnlineRegisterSerializer

class PreSchoolOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = PreSchoolOnlineRegister.objects.all()
    serializer_class = PreSchoolOnlineRegisterSerializer

class PrimarySchoolOnlineRegisterCreateAPIView(CreateAPIView):
    queryset = PrimarySchoolOnlineRegister.objects.all()
    serializer_class = PrimarySchoolOnlineRegisterSerializer

class EditionListAPIView(ListAPIView):
    queryset = EditionModel.objects.all()
    serializer_class = EditionSerializer

class EditionRetrieveAPIView(RetrieveAPIView):
    queryset = EditionModel.objects.all()
    serializer_class = EditionSerializer
    lookup_field = "id"




