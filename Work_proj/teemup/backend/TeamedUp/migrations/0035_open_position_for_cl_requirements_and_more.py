# Generated by Django 4.0.2 on 2022-08-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0034_extra_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='open_position_for_cl',
            name='requirements',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='open_position_for_un',
            name='requirements',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='league_resolution',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='sport_check',
            field=models.BooleanField(default=False),
        ),
    ]
