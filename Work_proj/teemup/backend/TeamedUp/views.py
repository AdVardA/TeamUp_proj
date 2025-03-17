"""views of django"""
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from django.contrib.auth.models import User, AnonymousUser
from django.core.mail import send_mail
import random

from .models import Profile, Unverified_Profile, Verificator, Univer_Profile, Club_Profile, Open_Position_for_Un
from .models import Achivment, Extra_Languages, Teem
from .models import Sport_Tag, Sport_Position_Tag, Language_Tag

from .forms import UserForm, Un_ProfileForm, Cl_ProfileForm, Un_Position_Form
from .forms import user_bio_form, user_academy_form, user_sport_form, user_letter_form
from .forms import User_Lang_Form, User_Ach_Form, User_Teem_Form, Verificator_Form


"""from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage"""

import random

EMAIL_HOST_USER = 'artnikitin2004@yandex.ru'
WEB_URL = "127.0.0.1:8000/"


"""def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('acc_active_email.html',{ 'user': user, 'domain': current_site.domain, 'uid':urlsafe_base64_encode(force_bytes(user.pk)), 'token' :account_activation_token.make_token(user),})
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            emailsend()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = SignupForm()

        rand = random.randint(0,100000)
        
        return render(request, 'signup.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        if user is not None and\
    account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
        # return redirect('home')
            return HttpResponse('Thank you for your email confirmation. Now you can login your account')
        else:
                return HttpResponse('Activation Link is invalid!')"""


def menu_user():
    """menu for user"""
    return [
        {'link': "/University", 'name': 'Университеты'},
        # {'link': "/Сlubs", 'name': 'Клубы'},
        {'link': "/Positions/?owner=", 'name': 'Позиции'},
        {'link': "/accounts/prof/", 'name': 'Профиль'},
        {'link': "/accounts/logout/", 'name': 'Выход'},
    ]


def menu_anther():
    """menu for ather"""
    return [
        {'link': "/Athletes", 'name': 'Спортсмены'},
        {'link': "/accounts/prof_un/", 'name': 'Профиль'},
        {'link': "/accounts/logout/", 'name': 'Выход'},
    ]


def web():
    """social"""
    return [
        {
            # facebook
            'link': 'https://www.facebook.com/Teamed-Up-363186321537325',
            'class': 'feather feather-facebook fea icon-sm fea-social',
            'path': 'M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z',
            'x': '-1000',
            'y': '-1000',
            'width': '-1000',
            'height': '-1000',
            'rx': '-1000',
            'ry': '-1000',
            'x1': '-1000',
            'y1': '-1000',
            'x2': '-1000',
            'y2': '-1000',
            'cx': '-1000',
            'cy': '-1000',
            'r': '-1000',
        },
        {
            # instagram
            'link': 'https://www.instagram.com/teamedup_recruitment/ ',
            'class': "feather feather-instagram fea icon-sm fea-social",
            'path': "M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z",
            'x': '2',
            'y': '2',
            'width': '20',
            'height': '20',
            'rx': '5',
            'ry': '5',
            'x1': '17.5',
            'y1': '6.5',
            'x2': '17.51',
            'y2': '6.5',
            'cx': '',
            'cy': '',
            'r': '',
        },

    ]

def code_cache(auth_code, mail):
    ans = ''
    code = str(auth_code) + str(auth_code)
    for i in range(len(code)):
        ans = ans + str(ord(code[i]) ^ ord(mail[i%len(mail)]))
    return ans
def company():
    """info for connect"""
    return [
        {
            'link': '',
            'name': ' About us'
        },
        {
            'link': '',
            'name': ' Services'
        },
        {
            'link': '',
            'name': ' Team'
        },
        {
            'link': '',
            'name': ' Pricing'
        },
        {
            'link': '',
            'name': ' Project'
        },
        {
            'link': '',
            'name': ' Careers'
        },
        {
            'link': '',
            'name': ' Blog'
        },
        {
            'link': '',
            'name': ' Login'
        },
    ]


def usfull_links():
    """info for move"""
    return [
        {
            'link': '/',
            'name': 'For sportmen'
        },
        {
            'link': '/start_un/',
            'name': 'For university'
        },
        # {'link': '/start_cl/','name': 'For club'},
        {
            'link': '',
            'name': 'Privacy Policy'
        },
        {
            'link': '',
            'name': 'Documentation'
        },
        {
            'link': '',
            'name': 'Changelog'
        },
        {
            'link': '',
            'name': 'Components'
        },
    ]


def user_dop_content():
    """main info for user"""
    return {
        'menu_user': menu_user(),
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),
    }


def ather_dop_content():
    """main info for ather"""
    return {
        'menu_ather': menu_anther(),
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),
    }


def start_user_link():
    """Info for start page"""
    return {
        'name': 'sportmen',
        'reg': '/accounts/login/',
        'enter': '/accounts/reg/',
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),
        'massage':"",
    }


def start_un_link():
    """Info for start page"""
    return {
        'name': 'university',
        'reg': '/accounts/login_Un/',
        'enter': '/accounts/reg_un/',
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),

    }


def start_cl_link():
    """Info for start page"""
    return {
        'name': 'clubs',
        'reg': '/accounts/login_Cl/',
        'enter': '/accounts/reg_cl/',
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),

    }


def start_user(request):
    """first page for user"""
    data = start_user_link()
    return render(request, 'start.html', data)


def start_un(request):
    """first page for un"""
    data = start_un_link()
    return render(request, 'start.html', data)


def start_cl(request):
    """first  page for cl"""
    data = start_cl_link()
    return render(request, 'start.html', data)


def uni(request):
    """page with un"""
    data = user_dop_content()
    data['Univer'] = Univer_Profile.objects.all().filter(flag=True)

    return render(request, 'Univers.html', data)


def clubs(request):
    """page with cl"""

    club = [
        {'png_link': '/static/main_files/campus.jpg',
         'name': 'ABC',
         'disc': 'qwertyuiop',
         'count_clubs': '2',
         'count_position': '123',
         'un_link': 'https://www.ox.ac.uk/'},
        {'png_link': '/static/main_files/campus.jpg',
         'name': 'ABC',
         'disc': 'qwertyuiop',
         'count_clubs': '2',
         'count_position': '123',
         'un_link': 'https://www.ox.ac.uk/'}
    ]
    data = user_dop_content()
    data["Club"] = club

    return render(request, 'Clubs.html', data)


def sports(requst):
    """page with sportsmen """
    positon = Profile.objects.all()
    data = ather_dop_content()
    data['Sports'] = positon

    return render(requst, "Sportsmen.html", data)


def show_res(request):
    """show user's res"""
    # 127.0.0.1:8000/Athletes/resume/?id=19
    data = {}
    indicator = request.GET.get('id')
    data['profile'] = Profile.objects.all().filter(id=indicator).first()
    data['lan'] = Extra_Languages.objects.all().filter(owner_id=indicator, flag=True).all()
    data['ach'] = Achivment.objects.all().filter(owner=indicator, flag=True).all()
    data['teems'] = Teem.objects.all().filter(owner=indicator, flag=True).all()

    return render(request, "show_user_res.html", data)


def pos(request):
    """page with pos"""

    owner = request.GET.get('owner')
    data = user_dop_content()
    if owner != '':
        data['pos'] = Open_Position_for_Un.objects.all().filter(active=True, owner=owner)
    else:
        data['pos'] = Open_Position_for_Un.objects.all().filter(active=True)
    return render(request, "Position.html", data)


class login_view_user(TemplateView):
    """enter for user"""

    def dispatch(self, request, *args, **kwargs):
        data = user_dop_content()
        if request.method == 'POST':
            name = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=name, password=password)
            try:
                if Profile.objects.filter(id=user) is not None:
                    if user is not None:
                        login(request, user)
                        return redirect('profile')
                    data['error'] = "Логин или пароль неправильные"
            except:
                if user is not None:
                    login(request, user)
                    return redirect('profile')

                data['error'] = "Логин или пароль неправильные"

        return render(request, "accounts/login.html", data)


class login_view_univer(TemplateView):
    """enter for un"""

    def dispatch(self, request, *args, **kwargs):
        data = ather_dop_content()
        if request.method == 'POST':
            name = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=name, password=password)
            try:
                if Profile.objects.filter(id=user) is not None:
                    if user is not None:
                        login(request, user)
                        return redirect('un_profile')

                    data['error'] = "Логин или пароль неправильные "

            except:
                if user is not None:
                    login(request, user)
                    return redirect('un_profile')
                data['error'] = "Логин или пароль неправильные "

        return render(request, "accounts/login.html", data)


class login_view_club(TemplateView):
    """enter for cl"""

    def dispatch(self, request, *args, **kwargs):
        data = ather_dop_content()
        if request.method == 'POST':
            name = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=name, password=password)
            try:
                if Profile.objects.filter(id=user) is not None:
                    if user is not None:
                        login(request, user)
                        return redirect('cl_profile')
                    data['error'] = "Логин или пароль неправильные"
            except:
                if user is not None:
                    login(request, user)
                    return redirect('cl_profile')

                data['error'] = "Логин или пароль неправильные"

        return render(request, "accounts/login.html", data)


class register_view_user(TemplateView):
    """regist for user"""

    def dispatch(self, request, instance=None, *args, **kwargs):
        data = user_dop_content()
        if request.method == 'POST':
            username = request.POST.get('username')

            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                try:
                    User.objects.create_user(str(username), email, password)
                except:
                    pass
                first_object = User.objects.get(username=username)
                status = create_unverified_user_profile(first_object,email)
                if status == 0:
                    return redirect(reverse("login"))
                if status == 1:
                    data["massage"] = "We already send 3 code for you. Please, use them or try later."
                # data['t']=first_object
                # return render(request, "accounts/reg.html", data)

        return render(request, "accounts/reg.html", data)

def code_generator():
    return str(random.randint(1000000,10000000))


def create_unverified_user_profile(instance,email):
    """create profile """
    try:
        new_user = Unverified_Profile.objects.create(user=instance)
    except:
        new_user = Unverified_Profile.objects.filter(user=instance)
    verification_code_sender(new_user,email)



def verification_code_sender(new_user,email):
    #try:
    print("\n",email,"\n")
    if new_user.counter()!=3:
        code = code_generator()
        print("\n\n\n",code,'\n\n\n')
        verificator = Verificator.objects.create(owner=new_user, code = code, verificator_page_id = code_cache(code, email))
        new_user.plus_one_to_counter()
        send_mail("TeamedUp project","You create unverified accaunt. Usw this code "+code+" for verified."\
                  +"Page for verefication : "+WEB_URL+"verefication?id="+verificator.get_page_id(),
                  EMAIL_HOST_USER,
                  [email],
                  fail_silently=False)
        print("127.0.0.1/verefication?id="+verificator.get_page_id())
    """except:
        send_mail(
            "TeamedUp project",
            "We already send to you 3 codes."+"Please, use last of those.",
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )"""

"""
Допсать функцию создающую страницу с полем для ввода индефикатора + сделать страницу обрабатывающую введенный код
если он правельный то создать профель для юзера
"""
def verification_code_page(request):
    """show user's res"""
    # 127.0.0.1:8000/Athletes/resume/?id=19
    data = {}
    print("\n",request.GET.get('code'),'\n')
    print(request.POST)
    if request.POST.get('code') is not None:
        indicator = request.GET.get('id')
        print("\n\nindicateor=", indicator, "\n\n")
        print(request.GET)

        if(len(indicator)<30):
            ver = Verificator.objects.all().filter(verificator_page_id=indicator).first()
            data = {}
            print("\n\n", ver, "\n\n")
            if ver is not None:
                code = request.POST.get('code')
                print("\n\n",code,"\n\n")
                print("\n\n", isinstance(code, int), "\n\n")
                print("\n\n", int(code) == ver.get_code(),ver.get_code(), "\n\n")
                if isinstance(int(code), int):
                    if int(code) == ver.get_code():
                        print("\n\n:)")
                        ver.owner.verificate()
                        create_user_profile(ver.owner.user)
                        Unverified_Profile.objects.all().filter(user=ver.owner.user).delete()
                        return redirect('login')
                    data["massage"] = "Wrong code."

    form = Verificator_Form()

    data['form'] = form
    return render(request, 'verification_page.html',data)

def create_user_profile(instance):
    """create profile """
    Profile.objects.create(user=instance)



class register_view_univer(TemplateView):
    """regist for un"""

    def dispatch(self, request, instance=None, *args, **kwargs):
        data = ather_dop_content()
        if request.method == 'POST':
            username = request.POST.get('username')

            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            link = request.POST.get('link')

            if password == password2:
                User.objects.create_user(str(username), email, password)
                first_object = User.objects.get(username=username)
                create_user_profile_un(first_object)
                Univer_Profile.objects.filter(id=first_object).update(link=link)
                # Univer_Profile.objects.filter(id=first_object).update(flag=True)

                return redirect(reverse("login_un"))
                # data['t']=first_object
                # return render(request, "accounts/reg.html", data)

        return render(request, "accounts/reg_ather.html", data)


def create_user_profile_un(instance):
    """create profile un"""
    Univer_Profile.objects.create(id=instance)


class register_view_club(TemplateView):
    """regist for cl"""

    def dispatch(self, request, instance=None, *args, **kwargs):
        data = ather_dop_content()
        if request.method == 'POST':
            username = request.POST.get('username')

            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            link = request.POST.get('link')

            if password == password2:
                User.objects.create_user(str(username), email, password)
                first_object = User.objects.get(username=username)
                create_user_profile_cl(first_object)
                Club_Profile.objects.filter(id=first_object).update(link=link)
                Club_Profile.objects.filter(id=first_object).update(flag=True)
                return redirect(reverse("login_cl"))
                # data['t']=first_object
                # return render(request, "accounts/reg.html", data)

        return render(request, "accounts/reg_ather.html", data)


def create_user_profile_cl(instance):
    """create profile cl"""
    Club_Profile.objects.create(id=instance)


class profile_page_user(TemplateView):
    """profile user"""

    def dispatch(self, request, *args, **kwargs):
        data = user_dop_content()
        first_object = Profile.objects.get(id=request.user.profile.id)
        data['lan'] = two_in_row(Extra_Languages.objects.all().filter(owner_id=first_object))
        data['ach'] = two_in_row(Achivment.objects.all().filter(owner_id=first_object))
        data['teems'] = two_in_row(Teem.objects.all().filter(owner_id=first_object))
        return render(request, "accounts/Profile_user.html", data)


class profile_page_univer(TemplateView):
    """profile un"""

    def dispatch(self, request, *args, **kwargs):
        data = ather_dop_content()
        try:
            data['pos'] = two_in_row(Open_Position_for_Un.objects.all().filter(
                owner_id=Univer_Profile.objects.get(id=request.user.univer_profile.id)))
        except:
            pass

        return render(request, "accounts/Profile_un.html", data)


class profile_page_club(TemplateView):
    """profile cl"""

    def dispatch(self, request, *args, **kwargs):
        data = ather_dop_content()

        return render(request, "accounts/Profile_cl.html", data)


@login_required
@transaction.atomic
def update_profile_user(request):
    """ update profile user """
    temp = None
    data = {}
    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=request.user)
        bio_form = user_bio_form(request.POST, request.FILES, instance=request.user.profile)
        academy_form = user_academy_form(request.POST, request.FILES, instance=request.user.profile)
        sport_form = user_sport_form(request.POST, request.FILES, instance=request.user.profile)
        flag = True

        '''if user_form.is_valid():
            user_form.save()
        else:
            data['error'] = '1'

            data['user_form'] = user_form
            data['bio_form'] = bio_form
            data['academy_form'] = academy_form
            data['sport_form'] = sport_form
            flag = False'''
        print(flag)
        if bio_form.is_valid() and flag:
            #            Profile.objects.filter(id=request.user.profile.id).update(user_flag=True)
            temp = request.user.profile
            temp.user_flag = True
            temp.save()
            bio_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '2'

            data['user_form'] = user_form
            data['bio_form'] = bio_form
            data['academy_form'] = academy_form
            data['sport_form'] = sport_form
            flag = False
        print(flag)
        if academy_form.is_valid() and flag:
            #            Profile.objects.filter(id=request.user.profile.id).update(user_flag=True)
            temp = Profile.objects.get(id=request.user.profile.id)
            temp.user_flag = True
            temp.save()
            academy_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error3'] = '3'

            data['user_form'] = user_form
            data['bio_form'] = bio_form
            data['academy_form'] = academy_form
            data['sport_form'] = sport_form
            flag = False
        print(flag)
        if sport_form.is_valid() and flag:
            #            Profile.objects.filter(id=request.user.profile.id).update(user_flag=True)
            sport_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error4'] = '4'

            data['user_form'] = user_form
            data['bio_form'] = bio_form
            data['academy_form'] = academy_form
            data['sport_form'] = sport_form
            flag = False
        print(flag)
        if flag:
            return redirect('profile')
        return render(request, 'accounts/prof_set.html', data)

    user_form = UserForm(instance=request.user)
    bio_form = user_bio_form(instance=request.user.profile)
    academy_form = user_academy_form(instance=request.user.profile)
    sport_form = user_sport_form(instance=request.user.profile)

    data['user_form'] = user_form
    data['bio_form'] = bio_form
    data['academy_form'] = academy_form
    data['sport_form'] = sport_form

    return render(request, 'accounts/prof_set.html', data)


@login_required
@transaction.atomic
def update_letter(request):
    """ update letter """

    data = {}
    if request.method == 'POST':
        letter_form = user_letter_form(request.POST, instance=request.user.profile)

        flag = True

        if letter_form.is_valid():
            letter_form.save()
        else:
            data['error'] = '1'

            data['letter_form'] = letter_form
            flag = False

        if flag:
            return redirect('profile')

        return render(request, '/accounts/prof_letter.html', data)

    letter_form = user_letter_form(instance=request.user.profile)

    data['letter_form'] = letter_form

    return render(request, 'accounts/prof_letter.html', data)


@login_required
@transaction.atomic
def update_profile_univer(request):
    """update profile un"""
    temp = None
    data = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        un_form = Un_ProfileForm(request.POST, instance=request.user.univer_profile)

        if user_form.is_valid():
            user_form.save()
            flag = True
        else:
            data['error'] = '1'

            data['user_form'] = user_form
            flag = False
        if un_form.is_valid() and flag:
            temp = request.user.univer_profile
            temp.flag = True
            temp.save()
            un_form.save()
            flag = True

            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '3'

            data['user_form'] = user_form
            data['un_form'] = un_form
            flag = False
        if flag:
            return redirect('un_profile')
        return render(request, 'accounts/prof_set_un.html', data)

    user_form = UserForm(instance=request.user)
    un_form = Un_ProfileForm(instance=request.user.univer_profile)

    data['user_form'] = user_form
    data['un_form'] = un_form

    return render(request, 'accounts/prof_set_un.html', data)


@login_required
@transaction.atomic
def update_profile_club(request):
    """update profile cl"""
    temp = None
    data = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        flag = True

        if user_form.is_valid():
            user_form.save()
        else:
            data['error'] = '1'

            data['user_form'] = user_form
            flag = False

        cl_form = Cl_ProfileForm(request.POST, instance=request.user.club_profile)
        if cl_form.is_valid() and flag:
            temp = request.user.club_profile
            temp.flag = True
            temp.save()
            cl_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['user_form'] = user_form
            data['cl_form'] = cl_form
            flag = False
        if flag:
            return redirect('cl_profile')
        return render(request, '/accounts/prof_set_cl.html', data)

    user_form = UserForm(instance=request.user)
    cl_form = Cl_ProfileForm(instance=request.user.club_profile)

    data['user_form'] = user_form
    data['cl_form'] = cl_form

    return render(request, 'accounts/prof_set_cl.html', data)


def two_in_row(temp):
    """ two in row """
    tem_data = []
    i = 0
    while i < len(temp):
        arr = []
        arr.append(temp[i])
        if (i + 1) < len(temp):
            arr.append(temp[i + 1])
        i += 2
        tem_data.append(arr)

    return tem_data


@login_required
@transaction.atomic
def create_position_univer(request):
    """create position un"""
    first_object = Univer_Profile.objects.get(id=request.user.univer_profile.id)
    first_object.open_position_for_un_set.create(owner_id=request.user.univer_profile.id_id)
    temp = Univer_Profile.objects.get(id=request.user.univer_profile.id)
    temp.count_pos += 1
    temp.save()
    return redirect('un_profile')


@login_required
@transaction.atomic
def set_position_univer(request):
    """set position un"""
    data = {}
    first_object = Univer_Profile.objects.get(id=request.user.univer_profile.id)
    second_object = Open_Position_for_Un.objects.all().filter(id=request.GET.get('id')).first()
    data['pos_flag'] = '1'
    if (request.method == 'POST') and (second_object.owner_id == first_object.id_id):
        flag = True
        data['last_info'] = [
            Open_Position_for_Un.objects.filter(id=request.GET.get('id')).first().active,
            Open_Position_for_Un.objects.filter(id=request.GET.get('id')).first().sport_name,
            Open_Position_for_Un.objects.filter(id=request.GET.get('id')).first().position,
            Open_Position_for_Un.objects.filter(id=request.GET.get('id')).first().grant,
            Open_Position_for_Un.objects.filter(id=request.GET.get('id')).first().requirements,
        ]
        data['second_ph']=Open_Position_for_Un.objects.filter(id=request.GET.get('id')).first().sport_name,

        un_pos_form = Un_Position_Form(request.POST, instance=Open_Position_for_Un.objects.filter(
            id=request.GET.get('id')).first())
        name = request.POST.get('name')
        teem_name = request.POST.get('teem_name')
        if un_pos_form.is_valid() and flag:
            tem = Open_Position_for_Un.objects.get(id=request.GET.get('id'))
            tem.name = name
            tem.teem_name = teem_name
            tem.save()
            un_pos_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['form'] = un_pos_form
            flag = False
        if flag:
            return redirect('un_profile')

        return render(request, 'accounts/many_forms.html', data)
    else:
        un_pos_form = Un_Position_Form(
            instance=Open_Position_for_Un.objects.filter(id=request.GET.get("id")).first())

    data['form'] = un_pos_form

    return render(request, 'accounts/many_forms.html', data)


@login_required
@transaction.atomic
def create_position_club(request):
    """create position un"""
    first_object = Club_Profile.objects.get(id=request.user.club_profile.id)
    first_object.open_position_for_cl_set.create(owner_id=request.user.club_profile.id_id)
    return redirect('un_profile')


@login_required
@transaction.atomic
def create_lang_user(request):
    """create lang user"""
    first_object = Profile.objects.get(id=request.user.profile.id)
    first_object.extra_languages_set.create(owner_id=request.user.profile.id)
    return redirect('profile')


@login_required
@transaction.atomic
def create_ach_user(request):
    """create achievement user"""
    first_object = Profile.objects.get(id=request.user.profile.id)
    first_object.achivment_set.create(owner_id=request.user.profile.id)
    return redirect('profile')


@login_required
@transaction.atomic
def create_teem_user(request):
    """create teem user"""
    first_object = Profile.objects.get(id=request.user.profile.id)
    first_object.teem_set.create(owner_id=request.user.profile.id)
    return redirect('profile')


@login_required
@transaction.atomic
def set_lang_user(request):
    """set lang user"""
    data = {}
    data['tabl'] = '1'
    first_object = Profile.objects.get(id=request.user.profile.id)
    second_object = Extra_Languages.objects.all().filter(id=request.GET.get('id')).first()
    if (request.method == 'POST') and (second_object.owner_id == first_object.id):
        flag = True
        data['last_info'] = (
            Extra_Languages.objects.filter(id=request.GET.get('id')).first().name,
            Extra_Languages.objects.filter(id=request.GET.get('id')).first().level
        )
        un_lan_form = User_Lang_Form(request.POST, instance=Extra_Languages.objects.filter(
            id=request.GET.get('id')).first())
        if un_lan_form.is_valid() and flag:
            un_lan_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['form'] = un_lan_form
            flag = False
        if flag:
            return redirect('profile')

        return render(request, 'accounts/many_forms.html', data)

    user_form = UserForm(instance=Extra_Languages.objects.all)
    un_lan_form = User_Lang_Form(
        instance=Extra_Languages.objects.filter(id=request.GET.get("id")).first())

    data['form'] = un_lan_form

    return render(request, 'accounts/many_forms.html', data)


@login_required
@transaction.atomic
def set_ach_user(request):
    """set achievement user"""
    data = {}
    first_object = Profile.objects.get(id=request.user.profile.id)
    second_object = Achivment.objects.all().filter(id=request.GET.get('id')).first()
    if (request.method == 'POST') and (second_object.owner_id == first_object.id):
        flag = True
        data['last_info'] = (
            Achivment.objects.filter(id=request.GET.get('id')).first().title_of_achiv,
            Achivment.objects.filter(id=request.GET.get('id')).first().type,
            Achivment.objects.filter(id=request.GET.get('id')).first().date,
        )
        ach_form = User_Ach_Form(request.POST, instance=Achivment.objects.filter(
            id=request.GET.get('id')).first())
        if ach_form.is_valid() and flag:
            ach_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['form'] = ach_form
            flag = False
        if flag:
            return redirect('profile')

        return render(request, 'accounts/many_forms.html', data)
    user_form = UserForm(instance=request.user.profile)
    ach_form = User_Ach_Form(
        instance=Achivment.objects.filter(id=request.GET.get("id")).first())

    data['form'] = ach_form

    return render(request, 'accounts/many_forms.html', data)


@login_required
@transaction.atomic
def set_teem_user(request):
    """set teem user"""
    data = {}
    first_object = Profile.objects.get(id=request.user.profile.id)
    second_object = Teem.objects.all().filter(id=request.GET.get('id')).first()
    if (request.method == 'POST') and (second_object.owner_id == first_object.id):
        flag = True
        data['last_info'] = (
            Teem.objects.filter(id=request.GET.get('id')).first().name,
            Teem.objects.filter(id=request.GET.get('id')).first().link
        )
        form = User_Teem_Form(request.POST, instance=Teem.objects.filter(
            id=request.GET.get('id')).first())
        if form.is_valid() and flag:
            form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['form'] = form
            flag = False
        if flag:
            return redirect('profile')

        return render(request, 'accounts/many_forms.html', data)

    user_form = UserForm(instance=request.user)
    form = User_Teem_Form(Teem.objects.filter(id=request.GET.get("id")).first(),
                          instance=Teem.objects.filter(id=request.GET.get("id")).first())

    data['form'] = form

    return render(request, 'accounts/many_forms.html', data)


@login_required
@transaction.atomic
def set_bio_user(request):
    """set bio user"""
    data = {}
    if request.method == 'POST':
        flag = True

        form = user_bio_form(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and flag:
            form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['form'] = form
            flag = False
        if flag:
            return redirect('profile')
        return render(request, 'accounts/many_forms.html', data)

    form = user_bio_form(instance=request.user.profile)

    data['form'] = form

    return render(request, 'accounts/many_forms.html', data)


@login_required
@transaction.atomic
def set_acd_user(request):
    """set ach user"""
    data = {}
    data['tabl'] = '1'
    if request.method == 'POST':
        flag = True

        form = user_academy_form(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and flag:
            Achivment.flag = True
            form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['form'] = form
            flag = False
        if flag:
            return redirect('profile')

        return render(request, 'accounts/many_forms.html', data)

    form = user_academy_form(instance=request.user.profile)

    data['form'] = form

    return render(request, 'accounts/many_forms.html', data)


@login_required
@transaction.atomic
def set_sport_user(request):
    """set sport user"""
    data = {}
    if request.method == 'POST':
        flag = True

        form = user_sport_form(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and flag:
            form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '4'

            data['form'] = form
            flag = False
        if flag:
            return redirect('profile')
        return render(request, 'accounts/many_forms.html', data)

    form = user_sport_form(instance=request.user.profile)

    data['form'] = form

    return render(request, 'accounts/many_forms.html', data)


@login_required
def login_out(request):
    """login out"""
    django_logout(request)
    return redirect('/')


def delete_pos(request):
    """delete pos"""
    first_object = Univer_Profile.objects.get(id=request.user.univer_profile.id)
    second_object = Open_Position_for_Un.objects.all().filter(id=request.GET.get('id')).first()
    if second_object.owner_id == first_object.id_id:
        second_object.delete()
        temp = Univer_Profile.objects.get(id=request.user.univer_profile.id)
        temp.count_pos -= 1
        temp.save()
    return redirect('un_profile')


def delete_lan(request):
    """delete lan"""
    first_object = Profile.objects.get(id=request.user.profile.id)
    second_object = Extra_Languages.objects.all().filter(id=request.GET.get('id')).first()
    if second_object.owner_id == first_object.id:
        second_object.delete()
    return redirect('profile')


def delete_ach(request):
    """delete ach"""
    first_object = Profile.objects.get(id=request.user.profile.id)
    second_object = Achivment.objects.all().filter(id=request.GET.get('id')).first()
    if second_object.owner_id == first_object.id:
        second_object.delete()
    return redirect('profile')


def delete_teem(request):
    """delete teem"""
    first_object = Profile.objects.get(id=request.user.profile.id)
    second_object = Teem.objects.all().filter(id=request.GET.get('id')).first()
    if second_object.owner_id == first_object.id:
        second_object.delete()
    return redirect('profile')
