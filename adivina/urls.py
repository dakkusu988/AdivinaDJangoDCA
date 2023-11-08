# Archivo urls.py de adivina

from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
]