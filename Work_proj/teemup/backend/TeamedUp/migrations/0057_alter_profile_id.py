# Generated by Django 4.0.2 on 2022-09-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0056_achivment_flag_extra_languages_flag_teem_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
