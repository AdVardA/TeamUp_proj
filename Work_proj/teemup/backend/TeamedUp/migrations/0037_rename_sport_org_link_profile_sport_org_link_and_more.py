# Generated by Django 4.0.2 on 2022-08-19 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0036_profile_letter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Sport_org_link',
            new_name='sport_org_link',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Sport_org_name',
            new_name='sport_org_name',
        ),
    ]