from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from service.models import (
    BranchModel, SeasonModel, BlockModel, ClassModel, SubjectModel,
    GroupModel, LanguageModel, StudentCategoryModel, StudentModel, TeacherModel,
    MonthModel, StudentPaymentInformationModel, TeacherPaymentInformationModel
)
from rest_framework.response import Response
from exam.models import CustomUser
from service.api.serializers import (
    BranchSerializer, SeasonSerializer, SeasonCreateSerializer, BlockSerializer, ClassSerializer, SubjectSerializer,
    GroupSerializer, LanguageSerializer, StudentCategorySerializer, StudentSerializer, StudentCreateSerializer, TeacherSerializer, TeacherCreateSerializer,
    StudentPaymentInformationUpdateSerializer
)
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework import status
from datetime import date, datetime


class BranchListAPIView(ListAPIView):
    def get_queryset(self):
        email = self.kwargs.get("email")
        account = get_object_or_404(CustomUser, email=email)
        if account.is_superuser:
            return BranchModel.objects.all()
        else:
            return BranchModel.objects.filter(
                branch_accountant__email=email
            )
    serializer_class = BranchSerializer
    # permission_classes = (IsAdminUser,)


class BranchSeasonListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return SeasonModel.objects.filter(branch_id=id)
    serializer_class = SeasonSerializer
    # permission_classes = (IsAdminUser,)


class BranchCreateAPIView(CreateAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)


class BranchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"


class SeasonStudentListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return StudentModel.objects.filter(season_id=id)
    serializer_class = StudentSerializer
    # permission_classes = (IsAdminUser,)


class SeasonCreateAPIView(CreateAPIView):
    queryset = SeasonModel.objects.all()
    serializer_class = SeasonCreateSerializer
    # permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = SeasonModel.objects.create(
            name=data['name'],
            branch=BranchModel.objects.get(pk=data['branch']),
        )
        serializer = self.get_serializer(data=data)
        months = [
            "Sentyabr", "Oktyabr", "Noyabr", "Dekabr", "Yanvar",
            "Fevral", "Mart", "Aprel", "May", "Iyun",
            "Iyul", "Avqust"
        ]
        if serializer.is_valid():
            for season_month in months:
                season_month_obj = MonthModel.objects.create(
                    name=season_month,
                    season=instance
                )

                instance.months.add(season_month_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SeasonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SeasonModel.objects.all()
    serializer_class = SeasonCreateSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


class StudentCategoryListCreateAPIView(ListCreateAPIView):
    queryset = StudentCategoryModel.objects.all()
    serializer_class = StudentCategorySerializer
    # permission_classes = (IsAdminUser,)


class StudentCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = StudentCategoryModel.objects.all()
    serializer_class = StudentCategorySerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


class CategorySeasonStudentListAPIView(ListAPIView):
    def get_queryset(self):
        season_id = self.kwargs.get("season_id")
        category_id = self.kwargs.get("category_id")
        category = get_object_or_404(StudentCategoryModel, id=category_id)

        return StudentModel.objects.filter(
            season_id=season_id,
            categories=category
        )
    serializer_class = StudentSerializer
    # permission_classes = (IsAdminUser,)


class StudentCreateAPIView(CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentCreateSerializer
    # permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = StudentModel.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number1=data['phone_number1'],
            phone_number2=data['phone_number2'],
            wp_number=data['wp_number'],
            status=data['status'],
            season=SeasonModel.objects.get(pk=data['season']),
            sector=data['sector'],
            specialty=data['specialty'],
            payment_date=data['payment_date'],
            payment_amount=data['payment_amount'],
        )
        if data['abiturient_class']:
            abiturient_class = ClassModel.objects.filter(
                pk=data['abiturient_class']).first()
            instance.abiturient_class = abiturient_class
            instance.save()
        if data['group']:
            group = GroupModel.objects.filter(pk=data['group']).first()
            instance.group = group
            instance.save()
        if data['language']:
            language = LanguageModel.objects.filter(
                pk=data['language']).first()
            instance.language = language
            instance.save()

        if data['dim_point']:
            instance.dim_point = data['dim_point']
            instance.save()

        for category in data['categories']:
            instance.categories.add(category)   

        for block in data['blocks']:
            instance.blocks.add(block)

        for subject in data['subjects']:
            instance.subjects.add(subject)

        for teacher in data['teachers']:
            instance.teachers.add(teacher)

        for category in data['categories']:
            months = MonthModel.objects.filter(season=data['season']).all()
            p_date = datetime.strptime(data['payment_date'], "%Y-%m-%d")
            mon = 8
            year = p_date.year
            for month in months:
                day = p_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28

                month_obj = StudentPaymentInformationModel.objects.create(
                    month=month,
                    student=instance,
                    category=StudentCategoryModel.objects.get(pk=category),
                    paid_date=None,
                    payment_date=date(year, mon, day),
                    payment_amount=data['payment_amount']
                )

        serializer = self.get_serializer(data=data)
        return Response(serializer.initial_data, status=status.HTTP_201_CREATED)

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentCreateSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"

    def get_object(self):
        pk = self.kwargs['id']
        return StudentModel.objects.get(pk=pk)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.get_serializer(
            instance, data=data)
        StudentPaymentInformationModel.objects.filter(student=instance).delete()
        
        for category in request.data['categories']:
            months = MonthModel.objects.filter(season=request.data['season']).all()
            p_date = datetime.strptime(request.data['payment_date'], "%Y-%m-%d")
            mon = 8
            year = p_date.year
            for month in months:
                day = p_date.day
                mon = mon + 1
                if mon == 13:
                    mon = 1
                    year = year + 1
                elif mon in (4, 6, 9, 11) and day == 31:
                    day = 30
                elif mon == 2 and day > 28:
                    day = 28

                month_obj = StudentPaymentInformationModel.objects.create(
                    month=month,
                    student=instance,
                    category=StudentCategoryModel.objects.get(pk=category),
                    paid_date=None,
                    payment_date=date(year, mon, day),
                    payment_amount=request.data['payment_amount']
                )


        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

class SeasonTeacherListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        return TeacherModel.objects.filter(season_id=id)
    serializer_class = TeacherSerializer
    # permission_classes = (IsAdminUser,)


class TeacherCreateAPIView(CreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherCreateSerializer
    # permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = request.data
        instance = TeacherModel.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            specialty=data['specialty'],
            section=data['section'],
            salary=data['salary'],
            phone_number1=data['phone_number1'],
            wp_number=data['wp_number'],
            status=data['status'],
            season=SeasonModel.objects.get(pk=data['season']),
            payment_date=data['payment_date'],
            payment_amount=data['payment_amount'],
        )

        months = MonthModel.objects.filter(season=data['season']).all()
        p_date = datetime.strptime(data['payment_date'], "%Y-%m-%d")
        mon = 8
        year = p_date.year
        for month in months:
            day = p_date.day
            mon = mon + 1
            if mon == 13:
                mon = 1
                year = year + 1
            elif mon in (4, 6, 9, 11) and day == 31:
                day = 30
            elif mon == 2 and day > 28:
                day = 28
            month_obj = TeacherPaymentInformationModel.objects.create(
                month=month,
                teacher=instance,
                payment_date=date(year, mon, day),
                payment_amount=data['payment_amount']
            )
        serializer = self.get_serializer(data=data)
        return Response(serializer.initial_data, status=status.HTTP_201_CREATED)


class TeacherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherCreateSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


class BlockListCreateAPIView(ListCreateAPIView):
    queryset = BlockModel.objects.all()
    serializer_class = BlockSerializer
    # permission_classes = (IsAdminUser,)


class BlockRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlockModel.objects.all()
    serializer_class = BlockSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


class ClassListCreateAPIView(ListCreateAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer
    # permission_classes = (IsAdminUser,)


class ClassRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = (IsAdminUser,)


class SubjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


class GroupListCreateAPIView(ListCreateAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = (IsAdminUser,)


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


class LanguageListCreateAPIView(ListCreateAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = (IsAdminUser,)


class LanguageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = (IsAdminUser,)
    lookup_field = "id"


# class AbiturientBlockListAPIView(ListAPIView):
#     queryset = AbiturientBlockModel.objects.all()
#     serializer_class = AbiturientBlockSerializer
#     permission_classes = (IsAdminUser,)

# class AbiturientClassListAPIView(ListAPIView):
#     queryset = AbiturientClassModel.objects.all()
#     serializer_class = AbiturientClassSerializer
#     permission_classes = (IsAdminUser,)

# class AbiturientSubjectListAPIView(ListAPIView):
#     queryset = AbiturientSubjectModel.objects.all()
#     serializer_class = AbiturientSubjectSerializer
#     permission_classes = (IsAdminUser,)

# class AbiturientGroupListAPIView(ListAPIView):
#     queryset = AbiturientGroupModel.objects.all()
#     serializer_class = AbiturientGroupSerializer
#     permission_classes = (IsAdminUser,)

# class AbiturientListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return AbiturientModel.objects.filter(student__season_id=id)
#     serializer_class = AbiturientSerializer
#     permission_classes = (IsAdminUser,)

# class BlockAbiturientListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         block = AbiturientBlockModel.objects.get(id=id)
#         return AbiturientModel.objects.filter(blocks=block)
#     serializer_class = AbiturientSerializer
#     permission_classes = (IsAdminUser,)

# class ClassAbiturientListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         abiturient_class = AbiturientClassModel.objects.get(id=id)
#         return AbiturientModel.objects.filter(abiturient_class=abiturient_class)
#     serializer_class = AbiturientSerializer
#     permission_classes = (IsAdminUser,)

# class SubjectAbiturientListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         subject = AbiturientSubjectModel.objects.get(id=id)
#         return AbiturientModel.objects.filter(subjects=subject)
#     serializer_class = AbiturientSerializer
#     permission_classes = (IsAdminUser,)

# class GroupAbiturientListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         group = AbiturientGroupModel.objects.get(id=id)
#         return AbiturientModel.objects.filter(group=group)
#     serializer_class = AbiturientSerializer
#     permission_classes = (IsAdminUser,)

# class MasterForeignLanguageListAPIView(ListAPIView):
#     queryset = MasterForeignLanguageModel.objects.all()
#     serializer_class = MasterForeignLanguageSerializer
#     permission_classes = (IsAdminUser,)

# class MasterSubjectListAPIView(ListAPIView):
#     queryset = MasterSubjectModel.objects.all()
#     serializer_class = MasterSubjectSerializer
#     permission_classes = (IsAdminUser,)

# class MasterGroupListAPIView(ListAPIView):
#     queryset = MasterGroupModel.objects.all()
#     serializer_class = MasterGroupSerializer
#     permission_classes = (IsAdminUser,)

# class MasterListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return MasterModel.objects.filter(student__season_id=id)
#     serializer_class = MasterSerializer
#     permission_classes = (IsAdminUser,)

# class ForeignLanguageMasterListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         language = MasterForeignLanguageModel.objects.get(id=id)
#         return MasterModel.objects.filter(language=language)
#     serializer_class = MasterSerializer
#     permission_classes = (IsAdminUser,)

# class SubjectMasterListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         subject = MasterSubjectModel.objects.get(id=id)
#         return MasterModel.objects.filter(subjects=subject)
#     serializer_class = MasterSerializer
#     permission_classes = (IsAdminUser,)

# class GroupMasterListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         group = MasterGroupModel.objects.get(id=id)
#         return MasterModel.objects.filter(group=group)
#     serializer_class = MasterSerializer
#     permission_classes = (IsAdminUser,)

# class MIQSubjectListAPIView(ListAPIView):
#     queryset = MIQSubjectModel.objects.all()
#     serializer_class = MIQSubjectSerializer
#     permission_classes = (IsAdminUser,)

# class MIQListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return MIQModel.objects.filter(student__season_id=id)
#     serializer_class = MIQSerializer
#     permission_classes = (IsAdminUser,)

# class SubjectMIQListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         subject = MIQSubjectModel.objects.get(id=id)
#         return MIQModel.objects.filter(subjects=subject)
#     serializer_class = MIQSerializer
#     permission_classes = (IsAdminUser,)

# class CivilServiceSubjectListAPIView(ListAPIView):
#     queryset = CivilServiceSubjectModel.objects.all()
#     serializer_class = CivilServiceSubjectSerializer
#     permission_classes = (IsAdminUser,)

# class CivilServiceListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return CivilServiceModel.objects.filter(student__season_id=id)
#     serializer_class = CivilServiceSerializer
#     permission_classes = (IsAdminUser,)

# class SubjectCivilServiceListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         subject = CivilServiceSubjectModel.objects.get(id=id)
#         return CivilServiceModel.objects.filter(subjects=subject)
#     serializer_class = CivilServiceSerializer
#     permission_classes = (IsAdminUser,)

# class ForeignLanguageListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return ForeignLanguageModel.objects.filter(student__season_id=id)
#     serializer_class = ForeignLanguageSerializer
#     permission_classes = (IsAdminUser,)

# class ComputerProgramTypeListAPIView(ListAPIView):
#     queryset = ComputerProgramTypeModel.objects.all()
#     serializer_class = ComputerProgramTypeSerializer
#     permission_classes = (IsAdminUser,)

# class ComputerCourseListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return ComputerCourseModel.objects.filter(student__season_id=id)
#     serializer_class = ComputerCourseSerializer
#     permission_classes = (IsAdminUser,)

# class ProgramTypeComputerCourseListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         program_type = ComputerProgramTypeModel.objects.get(id=id)
#         return ComputerCourseModel.objects.filter(program_types=program_type)
#     serializer_class = ComputerCourseSerializer
#     permission_classes = (IsAdminUser,)

# class AccountingListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return AccountingModel.objects.filter(student__season_id=id)
#     serializer_class = AccountingSerializer
#     permission_classes = (IsAdminUser,)

# class HighSchoolClassListAPIView(ListAPIView):
#     queryset = HighSchoolClassModel.objects.all()
#     serializer_class = HighSchoolClassSerializer
#     permission_classes = (IsAdminUser,)

# class HighSchoolSubjectListAPIView(ListAPIView):
#     queryset = HighSchoolSubjectModel.objects.all()
#     serializer_class = HighSchoolSubjectSerializer
#     permission_classes = (IsAdminUser,)

# class HighSchoolGroupListAPIView(ListAPIView):
#     queryset = HighSchoolGroupModel.objects.all()
#     serializer_class = HighSchoolGroupSerializer
#     permission_classes = (IsAdminUser,)

# class HighSchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return HighSchoolModel.objects.filter(student__season_id=id)
#     serializer_class = HighSchoolSerializer
#     permission_classes = (IsAdminUser,)

# class ClassHighSchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         highschool_class = HighSchoolClassModel.objects.get(id=id)
#         return HighSchoolModel.objects.filter(highschool_class=highschool_class)
#     serializer_class = HighSchoolSerializer
#     permission_classes = (IsAdminUser,)

# class SubjectHighSchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         subject = HighSchoolSubjectModel.objects.get(id=id)
#         return HighSchoolModel.objects.filter(subjects=subject)
#     serializer_class = HighSchoolSerializer
#     permission_classes = (IsAdminUser,)

# class GroupHighSchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         group = HighSchoolGroupModel.objects.get(id=id)
#         return HighSchoolModel.objects.filter(group=group)
#     serializer_class = HighSchoolSerializer
#     permission_classes = (IsAdminUser,)

# class PreSchoolSubjectListAPIView(ListAPIView):
#     queryset = PreSchoolSubjectModel.objects.all()
#     serializer_class = PreSchoolSubjectSerializer
#     permission_classes = (IsAdminUser,)

# class PreSchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return PreSchoolModel.objects.filter(student__season_id=id)
#     serializer_class = PreSchoolSerializer
#     permission_classes = (IsAdminUser,)

# class SubjectPreSchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         subject = PreSchoolSubjectModel.objects.get(id=id)
#         return PreSchoolModel.objects.filter(subjects=subject)
#     serializer_class = PreSchoolSerializer
#     permission_classes = (IsAdminUser,)

# class PrimarySchoolClassListAPIView(ListAPIView):
#     queryset = PrimarySchoolClassModel.objects.all()
#     serializer_class = PrimarySchoolClassSerializer
#     permission_classes = (IsAdminUser,)

# class PrimarySchoolSubjectListAPIView(ListAPIView):
#     queryset = PrimarySchoolSubjectModel.objects.all()
#     serializer_class = PrimarySchoolSubjectSerializer
#     permission_classes = (IsAdminUser,)

# class PrimarySchoolGroupListAPIView(ListAPIView):
#     queryset = PrimarySchoolGroupModel.objects.all()
#     serializer_class = PrimarySchoolGroupSerializer
#     permission_classes = (IsAdminUser,)

# class PrimarySchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         return PrimarySchoolModel.objects.filter(student__season_id=id)
#     serializer_class = PrimarySchoolSerializer
#     permission_classes = (IsAdminUser,)

# class ClassPrimarySchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         primaryschool_class = PrimarySchoolClassModel.objects.get(id=id)
#         return PrimarySchoolModel.objects.filter(primaryschool_class=primaryschool_class)
#     serializer_class = PrimarySchoolSerializer
#     permission_classes = (IsAdminUser,)

# class SubjectPrimarySchoolListAPIView(ListAPIView):
#     def get_queryset(self):
#         id = self.kwargs.get("id")
#         subject = PrimarySchoolSubjectModel.objects.get(id=id)
#         return PrimarySchoolModel.objects.filter(subjects=subject)
#     serializer_class = PrimarySchoolSerializer
#     permission_classes = (IsAdminUser,)

# class GroupPrimarySchoolListAPIView(ListAPIView):
    # def get_queryset(self):
    #     id = self.kwargs.get("id")
    #     group = PrimarySchoolGroupModel.objects.get(id=id)
    #     return PrimarySchoolModel.objects.filter(group=group)
    # serializer_class = PrimarySchoolSerializer
    # permission_classes = (IsAdminUser,)
