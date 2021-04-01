from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Resource 2 Tracking Index")

def add_provider(request):
    return HttpResponse("Add the provider here")