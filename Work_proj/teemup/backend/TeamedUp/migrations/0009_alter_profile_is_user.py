# Generated by Django 4.0.2 on 2022-08-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0008_profile_is_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
    ]
