# Generated by Django 4.0.2 on 2022-08-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0017_univer_profile_count_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='club_profile',
            name='count_pos',
            field=models.IntegerField(default=0),
        ),
    ]