from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from firstApp.models import CablePackage, CableProvider

# Create your views here.

def provider_function_view(request, provider_id):
    return HttpResponse('Here is your Provider: %s' % provider_id)
  

class PackageClassView(ListView):
    template_name = 'package_list_view.html'
    
    model = CablePackage
