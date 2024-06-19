from django.db import models

class NotificationModel(models.Model):
    STATUS = (
        ("O", "Oxunub"),
        ("OM", "Oxunmayıb")
    )
    TYPES = (
        ("D", "Silinmə"),
        ("A", "Əlavə olunma"),
        ("U", "Düzəliş"),
    )
    content = models.TextField("Məzmun")
    pub_date = models.DateTimeField("Yaranma tarixi", auto_now_add=True)
    status =  models.CharField("Status", max_length=2, choices=STATUS, default="OM")
    type = models.CharField("Əməliyyat", max_length=1, choices=TYPES)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Bildiriş"
        verbose_name_plural = "Bildirişlər"

    def __str__(self):
        return self.content

