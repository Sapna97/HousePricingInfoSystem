"""hpis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from broker.views import (
    register, view_profile, edit_profile, ProfileUpdate, change_password, user_login, success, user_logout,
    create_ad, AdvListView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('parameters/', parameters, name='parameters'),
    path('signup/', register, name='user_signup'),
    path('profile/', view_profile, name='my_profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/edit/update_more', ProfileUpdate.as_view(), name='update_profile'),
    path('password/', change_password, name='change_password'), 
    path('login/', user_login, name='user_login'),
    path('success/', success,  name= 'user_success'),
    path('profile/add_adv', create_ad, name='create_ad'),
    path('profile/adv_list', AdvListView.as_view(),  name='your_adv'),


]
