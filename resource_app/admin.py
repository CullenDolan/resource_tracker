from django.contrib import admin

from .models import Provider, Building, Schedule

admin.site.register(Provider)
admin.site.register(Building)
admin.site.register(Schedule)