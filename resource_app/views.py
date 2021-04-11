from django.shortcuts import render, get_object_or_404, redirect
from .models import Provider, Location, Schedule
from .forms import ProviderForm
from django.urls import reverse

def index(request):
    all_providers = Provider.objects.order_by('prov_lname')
    all_locations = Location.objects.order_by('building')
    context =  {'all_providers': all_providers,
                'all_locations': all_locations,}
    return render(request, 'resource_app/index.html', context)

def provider_detail(request, epic_id):
    provider = get_object_or_404(Provider, pk=epic_id)
    return render(request, 'resource_app/provider_detail.html', {'provider':provider})

def location_detail(request, id):
    location = get_object_or_404(Location, pk=id)
    return render(request, 'resource_app/location_detail.html', {'location':location})

def add_provider(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        #if form.is_valid():
        form.save()
        #return redirect(views.index)
    else:
        form = ProviderForm()
    return render(request, 'resource_app/add_provider.html', {'form':form})