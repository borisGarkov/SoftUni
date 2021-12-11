from django.contrib import admin

# Register your models here.
from pythons.pythons_app.models import Python


@admin.register(Python)
class PythonModel(admin.ModelAdmin):
    pass
