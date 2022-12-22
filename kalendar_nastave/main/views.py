from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import Voditelj, Racunalo, Aktivnost, Prostorija
from datetime import datetime
from django import forms

# kalsa za stvaranje forme godina
class YearForm(forms.Form):
    # odabir goidna od 1900 do 2100
    years = [(year, year) for year in range(1900, 2100)]

    # stvaramo ChoiceField 
    Godina_pocetka = forms.ChoiceField(choices=years)

# Create your views here.

class VoditeljList(ListView):
    model=Voditelj
    
class ProstorijaList(ListView):
    model=Prostorija

class RacunaloList(ListView):
    model=Racunalo

def homepage(request):
    return render(request, 'base_generic.html')

def aktivnosti(request):
    current_year = datetime.now().year
    form = YearForm(request.POST or None, initial={'Godina_pocetka': current_year})

    if request.method == 'POST' and form.is_valid():
        # da imamo samo godinu
        year = form.cleaned_data['Godina_pocetka']

        # filtiriranje DateTimeField po godini
        events = Aktivnost.objects.filter(vrijeme_pocetka__date__year=year)
    else:
        events = Aktivnost.objects.all()

    return render(request, 'main/aktivnosti.html', {'form': form, 'events': events})

