# Generated by Django 4.0.2 on 2022-08-30 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamedUp', '0044_achivment_date_achivment_title_of_achiv_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teems',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('link', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, to='TeamedUp.profile', unique=0)),
            ],
        ),
    ]
