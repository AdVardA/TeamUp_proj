import random

from django.core.files.storage import FileSystemStorage
from django.db import models
import datetime


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def code_generator():
    return str(random.randint(1000000,10000000))

class Small_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Unverified_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verificator_counter = models.IntegerField(default=0)
    email_flag = models.BooleanField(default=False, blank=False)
    def counter(self):
            return self.verificator_counter
    def plus_one_to_counter(self):
        self.verificator_counter+=1
    def verificate(self):
        self.email_flag = True
        self.verificator_counter = 0

#unique add this parametr for unique
class Verificator(models.Model):
    owner = models.ForeignKey(Unverified_Profile, on_delete=models.CASCADE, default=0)
    code = models.IntegerField(default=0)
    verificator_page_id = models.CharField(default=0, max_length=14)
    date = models.DateField(default=datetime.datetime.now())
    time = models.TimeField(default=datetime.datetime.now())
    def get_code(self):
        return self.code

    def get_page_id(self):
        return self.verificator_page_id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=1)
    id = models.IntegerField(primary_key=True)
    user_flag = models.BooleanField(default=False, blank=False)
    is_user = models.BooleanField(default=True, blank=False)


    # avatar = models.ImageField(upload_to='static/Users/data/photos/',default='static/Users/data/photos/temp.jpg',blank=False)

    ''' Bio '''
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=False)
    phone_num = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=100, blank=True)
    whats_app = models.BooleanField(default=True, blank=True)
    insta = models.CharField(max_length=50, blank=True)
    telega = models.CharField(max_length=50, blank=True, default='')
    agree_to_private_rule = models.BooleanField(default=False, blank=True)
    bio_check = models.BooleanField(default=False)

    ''' Academy '''
    eng_skill = models.CharField(max_length=2, blank=False)
    languages = models.CharField(max_length=150, blank=False)
    scholarship = models.BooleanField(default=False, blank=False)
    # school classes
    eng_class = models.IntegerField(default=0, blank=True)
    math_class = models.IntegerField(default=0, blank=True)
    natural_science_class = models.IntegerField(default=0, blank=True)
    additional_class = models.IntegerField(default=0, blank=True)
    social_science = models.IntegerField(default=0, blank=True)
    additional_courses = models.IntegerField(default=0, blank=True)
    # end classes
    # tests
    sat = models.BooleanField(default=False, blank=False)
    act = models.BooleanField(default=False, blank=False)
    toefl = models.BooleanField(default=False, blank=False)
    ielts = models.BooleanField(default=False, blank=False)
    # end tests

    ''' Sport '''
    sport = models.CharField(max_length=200, blank=False)
    ex = models.IntegerField(blank=False, default=0)
    position = models.CharField(max_length=200, blank=False)
    sport_org_name = models.CharField(max_length=200, blank=False)
    sport_org_link = models.CharField(max_length=200, blank=False)
    highlights_link = models.CharField(max_length=200, blank=True)
    stats_link = models.CharField(max_length=200, blank=True)
    live_stream_link = models.CharField(max_length=200, blank=True)
    pay_or_not = models.BooleanField(default=False, blank=False)
    hand = models.CharField(max_length=10, blank=True)
    height_inch = models.IntegerField(default=0, blank=True)
    height_cm = models.IntegerField(default=0, blank=True)
    weight_pound = models.IntegerField(default=0, blank=True)
    weight_kg = models.IntegerField(default=0, blank=True)
    league_resolution = models.BooleanField(default=False, blank=False)
    university_or_club = models.CharField(max_length=10, blank=True)
    national_teem = models.BooleanField(default=False)
    sport_check = models.BooleanField(default=False)

    ''' Letter '''
    letter = models.CharField(max_length=1500, blank=True)


class Achivment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, unique=0, primary_key=0, null=1)
    id = models.IntegerField(primary_key=1)
    title_of_achiv = models.CharField(max_length=75, blank=False, default='')
    type = models.CharField(max_length=9, blank=False, default='')
    date = models.DateField(null=True, blank=False)
    flag = models.BooleanField(default=False)


class Extra_Languages(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, unique=0, null=1)
    id = models.IntegerField(primary_key=1)
    name = models.CharField(max_length=25, blank=False)
    level = models.IntegerField(blank=False, default=0)
    flag = models.BooleanField(default=False)

class Teem(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, unique=0, null=1)
    id = models.IntegerField(primary_key=1)
    name = models.CharField(max_length=25, blank=True)
    link = models.CharField(max_length=50, blank=True)
    flag = models.BooleanField(default=False)



class Univer_Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, default=None, primary_key=True)
    active = models.BooleanField(default=False, blank=False)

    univers_name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=True)

    count_pos = models.IntegerField(default=0)

    is_un = models.BooleanField(default=True, blank=False)

    link = models.CharField(max_length=200, blank=True)

    flag = models.BooleanField(default=False, blank=True)




class Club_Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, default=None, primary_key=True)
    active = models.BooleanField(default=False, blank=False)

    club_name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=True)


    count_pos = models.IntegerField(default=0)

    is_cl = models.BooleanField(default=True, blank=False)

    link = models.CharField(max_length=200, blank=True)

    flag = models.BooleanField(default=False, blank=False)


class Open_Position_for_Un(models.Model):
    owner = models.ForeignKey(Univer_Profile, on_delete=models.CASCADE, unique=0, primary_key=0, null=1)
    id = models.IntegerField(primary_key=1)
    active = models.BooleanField(default=False, blank=False)

    teem_name = models.CharField(max_length=200, blank=True)
    sport_name = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=30, blank=True)
    grant = models.CharField(max_length=15, default='----')
    requirements = models.CharField(max_length=300, blank=True)
    close = models.BooleanField(default=False)


class Open_Position_for_Cl(models.Model):
    owner = models.ForeignKey(Univer_Profile, on_delete=models.CASCADE, unique=0, primary_key=0, null=1)
    id = models.IntegerField(primary_key=1)
    active = models.BooleanField(default=True, blank=False)

    sport_name = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=30, blank=True)
    requirements = models.CharField(max_length=300, blank=True)
    close = models.BooleanField(default=False)


class Tutor(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, default=None, primary_key=True)
    active = models.BooleanField(default=False, blank=False)

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=False)
    phone_num = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=100, blank=True)
    first_language = models.CharField(max_length=100, blank=True)
    second_language = models.CharField(max_length=100, blank=True)
    third_language = models.CharField(max_length=100, blank=False)
    whats_app = models.BooleanField(default=True, blank=True)
    telega = models.CharField(max_length=50, blank=True, default='')
    zoom = models.CharField(max_length=50, blank=True, default='')
    discord = models.CharField(max_length=50, blank=True, default='')
    about_me = models.CharField(max_length=500, blank=False,default='')

class Sport_Tag(models.Model):
    """Tag for sport's type

    Args:
        models (id): integer
        models (name): string
    """
    id = models.IntegerField(primary_key=1,blank=True)
    name = models.CharField(max_length=50, blank=1, default='')
    def __str__(self):
        return self.name
    def get_name(self):
        return self.name

class Sport_Position_Tag(models.Model):
    owner = models.ForeignKey(Sport_Tag, on_delete=models.CASCADE,  null=1)
    id = models.IntegerField(primary_key=1)
    name = models.CharField(max_length=50, blank=True)
    owner_name = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if self.owner:
            self.owner_name = self.owner.name
        super().save(*args, **kwargs) 
    def __str__(self):
        return  self.owner_name + ": " + self.name
    
class Sub_Sport_Position_Tag(models.Model):
    owner = models.ForeignKey(Sport_Position_Tag, on_delete=models.CASCADE,  null=1)
    id = models.IntegerField(primary_key=1)
    name = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return  self.owner.name + ": " + self.name


class Language_Tag(models.Model):
    """Tag for sport's type

    Args:
        models (id): integer
        models (name): string
    """
    id = models.IntegerField(primary_key=1,blank=True)
    name = models.CharField(max_length=50, blank=1, default='')


