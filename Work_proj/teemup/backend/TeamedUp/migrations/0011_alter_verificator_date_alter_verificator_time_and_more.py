# Generated by Django 5.1.5 on 2025-03-10 13:13

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0010_alter_sport_position_tag_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificator',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 3, 10, 13, 13, 19, 599379)),
        ),
        migrations.AlterField(
            model_name='verificator',
            name='time',
            field=models.TimeField(default=datetime.datetime(2025, 3, 10, 13, 13, 19, 599395)),
        ),
        migrations.CreateModel(
            name='Sub_Sport_Position_Tag',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('owner', models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, to='TeamedUp.sport_position_tag')),
            ],
        ),
    ]
