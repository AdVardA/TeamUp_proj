# Generated by Django 4.2.4 on 2024-04-06 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0076_alter_verificator_date_alter_verificator_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificator',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 4, 6, 10, 58, 2, 413496)),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 6, 10, 58, 2, 413514)),
        ),
    ]
