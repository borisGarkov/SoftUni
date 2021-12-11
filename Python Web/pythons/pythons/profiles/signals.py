from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from pythons.profiles.models import ProfileForm

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = ProfileForm(
            user=instance
        )
        profile.save()
