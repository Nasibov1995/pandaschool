from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from service.models import BranchModel


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, verbose_name="Ad")
    surname = models.CharField(max_length=50, verbose_name="Soyad")
    email = models.EmailField(unique=True, verbose_name="Email adresi")
    phone_number = models.CharField(
        max_length=50, verbose_name="Telefon nömrəsi", blank=True, null=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=False)
    is_superuser = models.BooleanField('superuser', default=False)
    is_student = models.BooleanField('student', default=False)
    is_accountant = models.BooleanField('Mühasib', default=False)
    branch = models.ForeignKey(BranchModel, verbose_name='Filial', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='branch_accountant')
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Hesab"
        verbose_name_plural = "Hesablar"

    def __str__(self):
        return self.name + " " + self.surname
