# Generated by Django 4.0.2 on 2022-08-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0030_achivment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='insta',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]