from django.db import models
from django.contrib.auth.models import User
import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    surname = models.CharField(max_length=100, default='')
    street = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=80, default='')
    post_code = models.CharField(max_length=6, default='')
    # phone_number = PhoneNumberField(unique=True)
    phone_number = models.CharField(max_length=9, default='')
    country = models.CharField(max_length=10, default='')
    birth_date = models.DateField(default=datetime.date.today)
    profile_picture = models.ImageField(default='profile_pictures/default_profile_pic.png', upload_to='profile_pictures')
    rules_agreement = models.BooleanField(default=False)
    pesel = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} profile"

