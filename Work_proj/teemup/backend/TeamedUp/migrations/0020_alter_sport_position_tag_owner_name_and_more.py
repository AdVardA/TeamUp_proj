# Generated by Django 5.1.5 on 2025-03-10 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0019_sport_position_tag_owner_name_alter_verificator_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport_position_tag',
            name='owner_name',
            field=models.CharField(default='None_id', max_length=50),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 3, 10, 15, 24, 24, 792958)),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='time',
            field=models.TimeField(default=datetime.datetime(2025, 3, 10, 15, 24, 24, 792975)),
        ),
    ]
