from django.db import models


# Create your models here.
class Python(models.Model):
    WORK_CATEGORIES = [
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Architecture', 'Architecture'),
    ]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    work_category = models.CharField(
        max_length=20,
        choices=WORK_CATEGORIES,
        default='IT'
    )
    image = models.ImageField(
        upload_to='images',
        blank=True
    )

    def __str__(self):
        return f"{self.name}, {self.work_category}"
