from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import Voditelj, Racunalo, Aktivnost, Prostorija
# Create your views here.

class VoditeljList(ListView):
    model=Voditelj

class AktivnostList(ListView):
    model=Aktivnost
    
class ProstorijaList(ListView):
    model=Prostorija

class RacunaloList(ListView):
    model=Racunalo



def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')
