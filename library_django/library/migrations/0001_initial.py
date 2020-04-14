# Generated by Django 3.0.5 on 2020-04-14 17:58

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=505, size=5)),
                ('publisher', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('time', models.IntegerField(default=14)),
                ('is_available', models.BooleanField(default=True)),
                ('edition', models.IntegerField(default=1)),
            ],
        ),
    ]
