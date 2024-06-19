from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_student", "is_accountant", "is_superuser",)
    list_filter = ("email", "is_student", "is_accountant", "is_superuser",)
    fieldsets = (
        (None, {"fields": ("email", "password", "name",
         "surname", "phone_number", "branch")}),
        ("Permissions", {"fields": ("is_staff",
         "is_active", "is_student", "is_superuser", "is_accountant",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "name", "surname", "phone_number",
                "is_staff", "is_active", "is_student", "is_accountant", "branch", "is_superuser"
            )}
         ),
    )
    search_fields = ("is_student", "is_accountant", "is_superuser",)
    ordering = ("email",)
    list_per_page = 20
