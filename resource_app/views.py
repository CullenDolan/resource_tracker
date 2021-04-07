from django.shortcuts import render, get_object_or_404
#from django.template import loader
# from django.http import HttpResponse
from .models import Provider


def index(request):
    all_providers = Provider.objects.order_by('prov_lname')
    context =  {'all_providers': all_providers}
    return render(request, 'resource_app/index.html', context)

def provider_detail(request, epic_id):
    provider = get_object_or_404(Provider, pk=epic_id)
    return render(request, 'resource_app/provider_detail.html', {'provider':provider})