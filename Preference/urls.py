from django.urls import path
from Preference.views import *

urlpatterns = [
    path('', parameters, name='parameters'),
    ]