from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from codes.models import Codes
from django.http import HttpResponseRedirect

class Index(ListView):
    model = Codes
    template_name = "indexc.html"

class Create(CreateView):
	model = Codes
	fields = ['name', 'text']

def show(request, codes_id):
    codes = get_object_or_404(Codes, pk=codes_id)
    return render(request, 'codes/show.html', {'codes': codes})

def delete(request, codes_id):
    codes = get_object_or_404(Codes, pk=codes_id).delete()
    return HttpResponseRedirect('/codes/index')