# Generated by Django 4.0.2 on 2022-10-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0060_remove_open_position_for_un_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open_position_for_un',
            name='position',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]