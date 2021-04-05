from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Provider


def home(request):
    all_providers = Provider.objects.order_by('prov_lname')
    template = loader.get_template('resource_app/index.html')
    context =  {
        'all_providers': all_providers
    }
    return HttpResponse(template.render(context, request))

def provider_detail(request, epic_id):
    return HttpResponse("You're looking at provider %s" % epic_id)