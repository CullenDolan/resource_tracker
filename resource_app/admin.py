from django.contrib import admin

from .models import Provider, Location, Schedule

admin.site.register(Provider)
admin.site.register(Location)
admin.site.register(Schedule)