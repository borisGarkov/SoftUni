from django.contrib import admin

# Register your models here.
from pythons.profile_auth.models import AppUser


@admin.register(AppUser)
class AppUserModel(admin.ModelAdmin):
    pass
