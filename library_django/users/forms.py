from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    surname = forms.CharField()
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ["username","name","surname", "email", "password1", "password2"]
