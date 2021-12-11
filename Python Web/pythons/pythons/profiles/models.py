from django.contrib.auth import get_user_model
from django.db import models

from pythons.profile_auth.models import AppUser

UserProfile = get_user_model()


# Create your models here.
class ProfileForm(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )

    last_name = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pics',
        blank=True
    )

    user = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        primary_key=True,
    )
