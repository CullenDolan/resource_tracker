from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Provider, Location, Schedule
from .forms import ProviderForm


class IndexView(generic.ListView):
    template_name = 'resource_app/index.html'
    context_object_name = 'latest_provider_list'

    def get_queryset(self):
        return Provider.objects.order_by('epic_id')[:10]


class DetailView(generic.DetailView):
    model = Provider
    template_name = 'resource_app/provider_detail.html'


# def location_detail(request, id):
#     location = get_object_or_404(Location, pk=id)
#     return render(request, 'resource_app/location_detail.html', {'location':location})


def add_provider(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('resource_app:index'), name='index')
    else:
        form = ProviderForm()
    return render(request, 'resource_app/add_provider.html', {'form':form})