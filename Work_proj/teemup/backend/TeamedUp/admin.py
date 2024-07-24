from django.contrib import admin
from .models import Profile, Univer_Profile, Club_Profile, Open_Position_for_Un, Open_Position_for_Cl, Extra_Languages, \
    Achivment, Teem, Unverified_Profile, Verificator

class Ach(admin.TabularInline):
    model = Achivment
    extra = 1
    def get_max_num(self, request, obj=None, **kwargs):
        return 10

class Extr_L(admin.TabularInline):
    model = Extra_Languages
    extra = 1
    def get_max_num(self, request, obj=None, **kwargs):
        return 5

class Tee(admin.TabularInline):
    model = Teem
    extra = 1
    def get_max_num(self, request, obj=None, **kwargs):
        return 10

class Ver(admin.TabularInline):
    model = Verificator
    extra = 0
    def has_change_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_max_num(self, request, obj=None, **kwargs):
        return 5


class Profel_id(admin.ModelAdmin):
    readonly_fields = ('id','user','is_user','user_flag','bio_check','agree_to_private_rule',
                       'scholarship',"sat","act","toefl","ielts",'whats_app','pay_or_not','national_teem'
                       ,'sport_check','league_resolution')
    list_display = ('id','user','country',)
    list_filter = ('id','user','country',)
    fieldsets = (
        (
            None,{
                'fields':('user','id','user_flag',"is_user")
            }),
        (
            "Bio",{
                'fields':(("first_name","last_name"),"birth_date","phone_num","country",
                          "whats_app","insta","telega","agree_to_private_rule","bio_check")
            }),(
            'Academy',{
                    'fields':("eng_skill",'languages','scholarship',
                              ("eng_class", 'math_class', 'natural_science_class',
                               "additional_class","social_science","additional_courses",),
                              ("sat","act","toefl","ielts",))

            }),(
            "Sport",{
                    'fields':(("sport","ex","position"),("sport_org_name","sport_org_link",
                              "highlights_link","stats_link","live_stream_link"),"pay_or_not",
                              ("hand","height_inch","height_cm","weight_pound","weight_kg"),
                              ("league_resolution","university_or_club","national_teem","sport_check"))
            })
    )
    inlines = [Ach,Extr_L,Tee]
    for i in inlines:
        i.readonly_fields = ('id',)


class Univer_Profile_id(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id','univers_name','country',"link",)
    #list_display_links = ()


class Club_Profile_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Open_Position_for_Un_id(admin.ModelAdmin):
    readonly_fields = ('id',)



class Open_Position_for_Cl_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Extra_Languages_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Achivment_id(admin.ModelAdmin):
    readonly_fields = ('id',)

class Teem_id(admin.ModelAdmin):
    readonly_fields = ('id',)

class Unverified_Profile_id(admin.ModelAdmin):
    readonly_fields = ('id','user',"verificator_counter", 'email_flag')
    inlines = [Ver]

class Verificator_id(admin.ModelAdmin):
    readonly_fields = ('id','owner','owner_for_reset_password','code','date','time','verificator_page_id')


admin.site.register(Profile, Profel_id)

admin.site.register(Univer_Profile, Univer_Profile_id)

admin.site.register(Club_Profile, Club_Profile_id)

admin.site.register(Open_Position_for_Un, Open_Position_for_Un_id)

admin.site.register(Open_Position_for_Cl, Open_Position_for_Cl_id)

admin.site.register(Extra_Languages, Extra_Languages_id)

admin.site.register(Achivment, Achivment_id)

admin.site.register(Teem, Teem_id)

admin.site.register(Unverified_Profile, Unverified_Profile_id)

admin.site.register(Verificator, Verificator_id)
