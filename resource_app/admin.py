from django.contrib import admin

from .models import Provider, BuildingChoice

admin.site.register(Provider)
admin.site.register(BuildingChoice)