__author__ = 'Chetan'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'event/$', views.event),
    url(r'hook/$', views.webhook),]