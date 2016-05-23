from django.views.generic import TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from robo.models import Robo
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

class AboutView(TemplateView):
    template_name = "about.html"

class Index(ListView):
    model = Robo
    template_name = "index.html"

class RoboCreate(CreateView):
	model = Robo
	fields = ['name', 'tribe']

def show(request, robo_id):
    robo = get_object_or_404(Robo, pk=robo_id)
    return render(request, 'robo/show.html', {'robo': robo})

def delete(request, robo_id):
    robo = get_object_or_404(Robo, pk=robo_id).delete()
    return HttpResponseRedirect('/robo/index')