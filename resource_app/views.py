from django.shortcuts import render, get_object_or_404
from .models import Provider, Location, Schedule
from django.urls import reverse

def index(request):
    all_providers = Provider.objects.order_by('prov_lname')
    context =  {'all_providers': all_providers}
    return render(request, 'resource_app/index.html', context)

def provider_detail(request, epic_id):
    provider = get_object_or_404(Schedule, pk=epic_id)
    return render(request, 'resource_app/provider_detail.html', {'provider':provider})

def location_detail(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, 'resource_app/location_detail.html', {'location':location})

# def add_schedule(request, epic_id):
#     new_schedule_slot = get_object_or_404(Schedule, )