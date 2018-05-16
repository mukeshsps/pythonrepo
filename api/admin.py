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



    
    

admin.site.register(Shop)
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(ShopType)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(WishList)


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
