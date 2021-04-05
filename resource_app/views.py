from django.shortcuts import render
from django.http import HttpResponse
from .models import Provider


def home(request):
    all_providers = Provider.objects.order_by('prov_lname')
    output = ', '.join([p.prov_lname for p in all_providers])
    return HttpResponse(output)

def provider_detail(request, epic_id):
    return HttpResponse("You're looking at provider %s" % epic_id)