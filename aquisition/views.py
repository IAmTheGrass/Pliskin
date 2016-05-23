from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from aquisition.models import Aquisition
from django.http import HttpResponseRedirect

class Index(ListView):
    model = Aquisition
    template_name = "indexa.html"

class Create(CreateView):
	model = Aquisition
	fields = ['robo', 'exploit']

def show(request, aquisition_id):
    aquisition = get_object_or_404(Aquisition, pk=aquisition_id)
    return render(request, 'aquisition/show.html', {'aquisition': aquisition})

def delete(request, aquisition_id):
    aquisition = get_object_or_404(Aquisition, pk=aquisition_id).delete()
    return HttpResponseRedirect('/aquisition/index')