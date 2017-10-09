"""
weatherservices URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^temperature/$', views.average_temperature, name='average_temperature'),
    url(r'^admin/', admin.site.urls),
]
