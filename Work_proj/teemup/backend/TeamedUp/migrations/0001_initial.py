# Generated by Django 5.1.5 on 2025-03-10 12:44

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


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
                ('club_name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('count_pos', models.IntegerField(default=0)),
                ('is_cl', models.BooleanField(default=True)),
                ('link', models.CharField(blank=True, max_length=200)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Language_Tag',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=1, serialize=False)),
                ('name', models.CharField(blank=1, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sport_Tag',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=1, serialize=False)),
                ('name', models.CharField(blank=1, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('active', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('phone_num', models.CharField(blank=True, max_length=12)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('first_language', models.CharField(blank=True, max_length=100)),
                ('second_language', models.CharField(blank=True, max_length=100)),
                ('third_language', models.CharField(max_length=100)),
                ('whats_app', models.BooleanField(blank=True, default=True)),
                ('telega', models.CharField(blank=True, default='', max_length=50)),
                ('zoom', models.CharField(blank=True, default='', max_length=50)),
                ('discord', models.CharField(blank=True, default='', max_length=50)),
                ('about_me', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Univer_Profile',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('active', models.BooleanField(default=False)),
                ('univers_name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('count_pos', models.IntegerField(default=0)),
                ('is_un', models.BooleanField(default=True)),
                ('link', models.CharField(blank=True, max_length=200)),
                ('flag', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_flag', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('phone_num', models.CharField(blank=True, max_length=12)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('whats_app', models.BooleanField(blank=True, default=True)),
                ('insta', models.CharField(blank=True, max_length=50)),
                ('telega', models.CharField(blank=True, default='', max_length=50)),
                ('agree_to_private_rule', models.BooleanField(blank=True, default=False)),
                ('bio_check', models.BooleanField(default=False)),
                ('eng_skill', models.CharField(max_length=2)),
                ('languages', models.CharField(max_length=150)),
                ('scholarship', models.BooleanField(default=False)),
                ('eng_class', models.IntegerField(blank=True, default=0)),
                ('math_class', models.IntegerField(blank=True, default=0)),
                ('natural_science_class', models.IntegerField(blank=True, default=0)),
                ('additional_class', models.IntegerField(blank=True, default=0)),
                ('social_science', models.IntegerField(blank=True, default=0)),
                ('additional_courses', models.IntegerField(blank=True, default=0)),
                ('sat', models.BooleanField(default=False)),
                ('act', models.BooleanField(default=False)),
                ('toefl', models.BooleanField(default=False)),
                ('ielts', models.BooleanField(default=False)),
                ('sport', models.CharField(max_length=200)),
                ('ex', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=200)),
                ('sport_org_name', models.CharField(max_length=200)),
                ('sport_org_link', models.CharField(max_length=200)),
                ('highlights_link', models.CharField(blank=True, max_length=200)),
                ('stats_link', models.CharField(blank=True, max_length=200)),
                ('live_stream_link', models.CharField(blank=True, max_length=200)),
                ('pay_or_not', models.BooleanField(default=False)),
                ('hand', models.CharField(blank=True, max_length=10)),
                ('height_inch', models.IntegerField(blank=True, default=0)),
                ('height_cm', models.IntegerField(blank=True, default=0)),
                ('weight_pound', models.IntegerField(blank=True, default=0)),
                ('weight_kg', models.IntegerField(blank=True, default=0)),
                ('league_resolution', models.BooleanField(default=False)),
                ('university_or_club', models.CharField(blank=True, max_length=10)),
                ('national_teem', models.BooleanField(default=False)),
                ('sport_check', models.BooleanField(default=False)),
                ('letter', models.CharField(blank=True, max_length=1500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Extra_Languages',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('level', models.IntegerField(default=0)),
                ('flag', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, to='TeamedUp.profile', unique=0)),
            ],
        ),
        migrations.CreateModel(
            name='Achivment',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('title_of_achiv', models.CharField(default='', max_length=75)),
                ('type', models.CharField(default='', max_length=9)),
                ('date', models.DateField(null=True)),
                ('flag', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, primary_key=0, to='TeamedUp.profile', unique=0)),
            ],
        ),
        migrations.CreateModel(
            name='Small_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sport_Position_Tag',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('owner', models.OneToOneField(null=1, on_delete=django.db.models.deletion.CASCADE, to='TeamedUp.sport_tag')),
            ],
        ),
        migrations.CreateModel(
            name='Teem',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25)),
                ('link', models.CharField(blank=True, max_length=50)),
                ('flag', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, to='TeamedUp.profile', unique=0)),
            ],
        ),
        migrations.CreateModel(
            name='Open_Position_for_Un',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('active', models.BooleanField(default=False)),
                ('teem_name', models.CharField(blank=True, max_length=200)),
                ('sport_name', models.CharField(blank=True, max_length=30)),
                ('position', models.CharField(blank=True, max_length=30)),
                ('grant', models.CharField(default='----', max_length=15)),
                ('requirements', models.CharField(blank=True, max_length=300)),
                ('close', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, primary_key=0, to='TeamedUp.univer_profile', unique=0)),
            ],
        ),
        migrations.CreateModel(
            name='Open_Position_for_Cl',
            fields=[
                ('id', models.IntegerField(primary_key=1, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('sport_name', models.CharField(blank=True, max_length=30)),
                ('position', models.CharField(blank=True, max_length=30)),
                ('requirements', models.CharField(blank=True, max_length=300)),
                ('close', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, primary_key=0, to='TeamedUp.univer_profile', unique=0)),
            ],
        ),
        migrations.CreateModel(
            name='Unverified_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verificator_counter', models.IntegerField(default=0)),
                ('email_flag', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Verificator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('verificator_page_id', models.CharField(default=0, max_length=14)),
                ('date', models.DateField(default=datetime.datetime(2025, 3, 10, 12, 44, 9, 995732))),
                ('time', models.TimeField(default=datetime.datetime(2025, 3, 10, 12, 44, 9, 995748))),
                ('owner', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='TeamedUp.unverified_profile')),
            ],
        ),
    ]
