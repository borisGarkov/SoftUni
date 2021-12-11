from django import forms
from django.core.validators import MinLengthValidator


def validate_dot(value):
    if '.' in value:
        raise forms.ValidationError('\'.\' is present in value')


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        validators=[
            validate_dot,
            MinLengthValidator(4),
        ]
    )
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'placeholder': 'Enter some text here'
            },
        )
    )
    state = forms.BooleanField()
    password = forms.CharField(widget=forms.PasswordInput())
