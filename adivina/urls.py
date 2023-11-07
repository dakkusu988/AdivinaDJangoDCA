# Archivo urls.py de task

from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
]