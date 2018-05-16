"""EMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api import views as auth_views
#from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    #url(r'^login/$', LoginView.as_view(), name='login'),
]
admin.site.site_header = ("E-Mall Site Administration")
admin.site.site_title = ("My E-Mall Site Admin")
#admin.site.site_header = "E_Mall Site Administration"
#admin.site.site_title = "E-Mall Site Admin"

#admin.site.site_header = 'Coffeehouse admin'
#admin.site.site_title = 'Coffeehouse admin'
admin.site.site_url = 'https://www.facebook.com'
admin.site.index_title = 'Mukesh site'
#admin.empty_value_display = '**Empty**