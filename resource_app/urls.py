"""
map the functions in resource_app/views.py as views to be shown to users
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]