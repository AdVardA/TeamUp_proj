# Generated by Django 4.2.4 on 2024-03-30 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0072_alter_verificator_date_alter_verificator_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificator',
            name='code',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 30, 10, 32, 45, 850988)),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 3, 30, 10, 32, 45, 851047)),
        ),
    ]