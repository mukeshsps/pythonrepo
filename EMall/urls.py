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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^login/$', auth_views.login, name='login'),
]
admin.site.site_header = ("E-Mall Site Administration")#Modify admin Site header
admin.site.site_title = ("My E-Mall Site Admin")#Modify admin site title
admin.site.site_url = 'https://www.facebook.com'#Place your site url here
admin.site.index_title = 'Mukesh site'#Modify admin site index page title
