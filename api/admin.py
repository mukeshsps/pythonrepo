from django.contrib import admin
from .models import Mall
from .models import Shop
from api.models import Category, ShopType, Product, ProductType, UserProfile,\
    Order, WishList
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from api.form import UserChangeForm
#from django.contrib.auth.admin import UserAdmin
#from api.form import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.



    
    
#admin.site.register(Mall)
admin.site.register(Shop)
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(ShopType)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(WishList)
#admin.site.empty_value_display = '(None)'
#admin.site.register(Cart)
# we can register more than on model class at admin site in django 2.0
#@admin.register(Employee, Mall, ShopType)// used for custom admin site( site=custom_admin_site)
#@admin.register(WishList)
#class AuthorAdmin(admin.ModelAdmin):
 #  pass
#class FlatPageAdmin(admin.ModelAdmin):
 #   fields = ('url', 'title', 'content')
    
"""class UserProfileinline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address')
    
##class UserAdmin(BaseUserAdmin):
    ##inlines = (UserProfileinline, )
admin.autodiscover()
admin.site.unregister(User)
admin.site.register(UserProfile, UserProfileAdmin)"""


"""class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'address', 'phone')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)"""


class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=("E-mail"), max_length=75)

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'password1', 'password2',)
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class UserProfileinline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User'
class UserAdmin(BaseUserAdmin):
    #form = UserChangeForm
    inlines = (UserProfileinline, )
    model = User
    list_per_page = 15 
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)   

#class UserAdmin(admin.ModelAdmin):
    #model = User
    #list_per_page = 5 
    


