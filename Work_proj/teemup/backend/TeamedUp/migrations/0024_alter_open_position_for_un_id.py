# Generated by Django 4.0.2 on 2022-08-09 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0023_alter_open_position_for_un_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open_position_for_un',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='TeamedUp.univer_profile', unique=0),
        ),
    ]
