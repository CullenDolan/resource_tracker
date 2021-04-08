from django.contrib import admin

from .models import Provider, Building

admin.site.register(Provider)
admin.site.register(Building)