# Generated by Django 4.0.2 on 2022-07-28 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club_Profile',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('active', models.BooleanField(default=False)),
                ('link', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Univer_Profile',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('active', models.BooleanField(default=False)),
                ('link', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agree_with_site_rule', models.BooleanField(default=False)),
                ('birth_date', models.DateField(null=True)),
                ('phone_num', models.CharField(blank=True, max_length=12)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('whats_app', models.BooleanField(blank=True, default=True)),
                ('insta', models.CharField(max_length=50)),
                ('eng_skill', models.CharField(max_length=2)),
                ('languages', models.CharField(max_length=150)),
                ('sport', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('Sport_org_name', models.CharField(max_length=200)),
                ('Sport_org_link', models.CharField(max_length=200)),
                ('pay_or_not', models.BooleanField(default=False)),
                ('highlights_link', models.CharField(blank=True, max_length=200)),
                ('hand', models.CharField(blank=True, max_length=10)),
                ('Height_inch_and_cm', models.CharField(blank=True, max_length=100)),
                ('Weight_pound_and_kg', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
