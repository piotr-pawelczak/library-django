# Generated by Django 3.0.3 on 2020-04-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200426_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_pictures/default_profile_pic.png', upload_to='profile_pictures'),
        ),
    ]
