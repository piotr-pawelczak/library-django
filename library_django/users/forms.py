from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    surname = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    post_code = forms.CharField()
    phone_number = forms.IntegerField()
    country = forms.CharField()
    birth_date = forms.DateField()
    profile_picture = forms.ImageField(required=False)
    pesel = forms.IntegerField()
    rules_agreement = forms.BooleanField(label='I have read and agree to the Terms and Conditions and Privacy Policy ')

    class Meta:
        model = User
        fields = ["username", 'name',  'surname', 'email', 'street', 'city', 'post_code', 'phone_number', 'country',
                  'birth_date', 'profile_picture', 'pesel', 'rules_agreement', "password1", "password2"]

