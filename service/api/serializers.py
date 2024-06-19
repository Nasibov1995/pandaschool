from rest_framework import serializers
from service.models import (
    BranchModel, SeasonModel, BlockModel, ClassModel, SubjectModel,
    GroupModel, LanguageModel, StudentCategoryModel, StudentModel, TeacherModel,
)
from rest_framework import serializers
from service.models import (
    MonthModel, TeacherPaymentInformationModel, StudentPaymentInformationModel
)
from drf_writable_nested import WritableNestedModelSerializer


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchModel
        fields = "__all__"


class MonthSeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthModel
        fields = "__all__"


class SeasonSerializer(serializers.ModelSerializer):
    branch = serializers.SlugRelatedField(
        queryset=BranchModel.objects.all(), slug_field="name")

    season_months = MonthSeasonSerializer(
        many=True, read_only=True, source='months')

    class Meta:
        model = SeasonModel
        fields = ['id', 'name', 'start_date',
                  'end_date', 'branch', 'season_months']


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockModel
        fields = "__all__"


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = "__all__"


class StudentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCategoryModel
        fields = "__all__"


class MonthSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()

    class Meta:
        model = MonthModel
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()

    class Meta:
        model = TeacherModel
        fields = "__all__"


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()
    abiturient_class = ClassSerializer()
    group = GroupSerializer()
    categories = StudentCategorySerializer(many=True)
    teachers = TeacherSerializer(many=True)
    blocks = BlockSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = StudentModel
        fields = "__all__"


class StudentCreateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=StudentCategoryModel.objects.all(), many=True, required=False)
    blocks = serializers.PrimaryKeyRelatedField(queryset=BlockModel.objects.all(), many=True, required=False)
    subjects = serializers.PrimaryKeyRelatedField(queryset=SubjectModel.objects.all(), many=True, required=False)
    teachers = serializers.PrimaryKeyRelatedField(queryset=TeacherModel.objects.all(), many=True, required=False)

    class Meta:
        model = StudentModel
        fields = '__all__'


class SeasonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeasonModel
        fields = ['id', 'name', 'branch']


class TeacherPaymentInformationSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    month = MonthSerializer()

    class Meta:
        model = TeacherPaymentInformationModel
        fields = "__all__"


class TeacherPaymentInformationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherPaymentInformationModel
        fields = "__all__"


class StudentPaymentInformationSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    month = MonthSerializer()
    category = StudentCategorySerializer()

    class Meta:
        model = StudentPaymentInformationModel
        fields = "__all__"


class StudentPaymentInformationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentPaymentInformationModel
        fields = "__all__"

# class AbiturientBlockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AbiturientBlockModel
#         fields = "__all__"

# class AbiturientClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AbiturientClassModel
#         fields = "__all__"

# class AbiturientSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AbiturientSubjectModel
#         fields = "__all__"

# class AbiturientGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AbiturientGroupModel
#         fields = "__all__"

# class AbiturientSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     blocks = AbiturientBlockSerializer(many=True)
#     abiturient_class = serializers.SlugRelatedField(queryset=AbiturientClassModel.objects.all(), slug_field="name")
#     subjects = AbiturientSubjectSerializer(many=True)
#     group = serializers.SlugRelatedField(queryset=AbiturientGroupModel.objects.all(), slug_field="name")

#     class Meta:
#         model = AbiturientModel
#         fields = "__all__"

# class MasterForeignLanguageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MasterForeignLanguageModel
#         fields = "__all__"

# class MasterSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MasterSubjectModel
#         fields = "__all__"

# class MasterGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MasterGroupModel
#         fields = "__all__"

# class MasterSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     language = serializers.SlugRelatedField(queryset=MasterForeignLanguageModel.objects.all(), slug_field="name")
#     subjects = MasterSubjectSerializer(many=True)
#     group = serializers.SlugRelatedField(queryset=MasterGroupModel.objects.all(), slug_field="name")

#     class Meta:
#         model = MasterModel
#         fields = "__all__"

# class MIQSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MIQSubjectModel
#         fields = "__all__"

# class MIQSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     subjects = MIQSubjectSerializer(many=True)

#     class Meta:
#         model = MIQModel
#         fields = "__all__"

# class CivilServiceSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CivilServiceSubjectModel
#         fields = "__all__"

# class CivilServiceSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     subjects = CivilServiceSubjectSerializer(many=True)

#     class Meta:
#         model = CivilServiceModel
#         fields = "__all__"

# class ForeignLanguageSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()

#     class Meta:
#         model = ForeignLanguageModel
#         fields = "__all__"

# class ComputerProgramTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ComputerProgramTypeModel
#         fields = "__all__"

# class ComputerCourseSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     program_types = ComputerProgramTypeSerializer(many=True)

#     class Meta:
#         model = ComputerCourseModel
#         fields = "__all__"

# class AccountingSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()

#     class Meta:
#         model = AccountingModel
#         fields = "__all__"

# class HighSchoolClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HighSchoolClassModel
#         fields = "__all__"

# class HighSchoolSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HighSchoolSubjectModel
#         fields = "__all__"

# class HighSchoolGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HighSchoolGroupModel
#         fields = "__all__"

# class HighSchoolSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     highschool_class = serializers.SlugRelatedField(queryset=HighSchoolClassModel.objects.all(), slug_field="name")
#     subjects = HighSchoolSubjectSerializer(many=True)
#     group = serializers.SlugRelatedField(queryset=HighSchoolGroupModel.objects.all(), slug_field="name")

#     class Meta:
#         model = HighSchoolModel
#         fields = "__all__"

# class PreSchoolSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PreSchoolSubjectModel
#         fields = "__all__"

# class PreSchoolSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     subjects = PreSchoolSubjectSerializer(many=True)

#     class Meta:
#         model = PreSchoolModel
#         fields = "__all__"

# class PrimarySchoolClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrimarySchoolClassModel
#         fields = "__all__"

# class PrimarySchoolSubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrimarySchoolSubjectModel
#         fields = "__all__"

# class PrimarySchoolGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrimarySchoolGroupModel
#         fields = "__all__"

# class PrimarySchoolSerializer(serializers.ModelSerializer):
#     student = StudentSerializer()
#     primaryschool_class = serializers.SlugRelatedField(queryset=PrimarySchoolClassModel.objects.all(), slug_field="name")
#     subjects = PrimarySchoolSubjectSerializer(many=True)
#     group = serializers.SlugRelatedField(queryset=PrimarySchoolGroupModel.objects.all(), slug_field="name")

#     class Meta:
#         model = PrimarySchoolModel
#         fields = "__all__"
