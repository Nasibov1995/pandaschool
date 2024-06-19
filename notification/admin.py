from django.contrib import admin
from notification.models import NotificationModel
from django.contrib import messages

@admin.register(NotificationModel)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "pub_date", "status")
    actions = ["mark_as_read", "mark_as_unread"]
    readonly_fields = ("content", "status", "type")

    @admin.action(description="Seçilmiş bildirişləri oxunmuş kimi işarələ")
    def mark_as_read(self, request, queryset):
        queryset.update(status="O")
        self.message_user(request, "Seçilmiş bildirişlər oxunmuş kimi işarələndi.", messages.SUCCESS)
    
    @admin.action(description="Seçilmiş bildirişlər oxunmamış kimi işarələ")
    def mark_as_unread(self, request, queryset):
        queryset.update(status="OM")
        self.message_user(request, "Seçilmiş bildirişlər oxunmamış kimi işarələndi.", messages.SUCCESS)


