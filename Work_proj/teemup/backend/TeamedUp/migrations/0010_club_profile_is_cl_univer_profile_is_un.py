# Generated by Django 4.0.2 on 2022-08-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0009_alter_profile_is_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='club_profile',
            name='is_cl',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='univer_profile',
            name='is_un',
            field=models.BooleanField(default=True),
        ),
    ]