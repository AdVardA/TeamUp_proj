# Generated by Django 4.0.2 on 2022-07-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0002_alter_profile_agree_with_site_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Agree_with_site_rule',
            field=models.BooleanField(default=False),
        ),
    ]