## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *
# Defining a factory
class RacunaloFactory(DjangoModelFactory):
    class Meta:
        model = Racunalo
    id_racunala = factory.Faker("pyint")
    marka  = factory.Faker("sentence", nb_words=1)
    tip = factory.Faker("sentence", nb_words=1)
    operacijski_sustav = factory.Faker("sentence", nb_words=1)
    mreza = factory.Faker("pybool")


class ProstorijaFactory(DjangoModelFactory):
    class Meta:
        model = Prostorija
        # da bude unique
        django_get_or_create = ('glavno_racunalo',)

    broj_prostorije = factory.Faker("random_int", max=50)
    kat = factory.Faker("random_int", max=10)
    naziv_prostorije = factory.Faker("sentence", nb_words=4)
    glavno_racunalo = factory.Iterator(Racunalo.objects.all())

class VoditeljFactory(DjangoModelFactory):
    class Meta:
        model = Voditelj
    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    email = factory.Faker("email")
    adresa = factory.Faker("address")
    telefon = factory.Faker("phone_number")

class AktivnostFactory(DjangoModelFactory):
    class Meta:
        model = Aktivnost
    naziv = factory.Faker("sentence", nb_words=3)
    opis = factory.Faker("sentence", nb_words=25)
    vrijeme_pocetka =  factory.Faker("date_time")
    vrijeme_zavrsetka = factory.Faker("date_time")
    prostorija_izvodjenja = factory.Iterator(Prostorija.objects.all())

