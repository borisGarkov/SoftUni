from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def page_count_validator(value):
    if value <= 0:
        raise ValidationError('Pages cannot be zero or negative.')


# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        validators=[
            MinValueValidator(1),
            page_count_validator
        ],
    )
    description = models.CharField(
        max_length=100,
        default='',
    )
    author = models.CharField(
        max_length=20,
    )
