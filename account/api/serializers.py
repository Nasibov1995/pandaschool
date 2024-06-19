from rest_framework import serializers
from account.models import CustomUser
from rest_framework.validators import UniqueValidator


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'surname', 'password', 'phone_number',
                  'is_student',  'is_accountant', 'branch', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'name': {'required': True},
            'surname': {'required': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            phone_number=validated_data['phone_number'],
            is_staff=validated_data['is_staff'],
            is_student=validated_data['is_student'],
            is_superuser=validated_data['is_superuser'],
            is_accountant=validated_data['is_accountant'],
            branch=validated_data['branch']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
