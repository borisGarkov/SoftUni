from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', )


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=15
    )
    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput()
    )
