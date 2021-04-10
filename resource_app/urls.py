"""
map the functions in resource_app/views.py as views to be shown to users
"""

from django.urls import path
from . import views
app_name = 'resource_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('provider/<int:epic_id>/', views.provider_detail, name='provider_detail'),
    path('location/<int:id>/', views.location_detail, name='location_detail')
    #path('<int:epic_id>/add_schedule/', views.add_schedule, name='add_schedule'),
]