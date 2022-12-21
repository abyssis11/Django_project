from django.contrib import admin
from .models import Aktivnost, Voditelj, Prostorija, Racunalo
lista = [Aktivnost, Prostorija, Voditelj, Racunalo]
admin.site.register(lista)