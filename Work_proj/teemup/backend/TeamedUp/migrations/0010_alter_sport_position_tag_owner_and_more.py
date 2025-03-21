# Generated by Django 5.1.5 on 2025-03-10 13:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0009_alter_verificator_date_alter_verificator_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport_position_tag',
            name='owner',
            field=models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, to='TeamedUp.sport_tag'),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 3, 10, 13, 2, 20, 983612)),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='time',
            field=models.TimeField(default=datetime.datetime(2025, 3, 10, 13, 2, 20, 983627)),
        ),
    ]
