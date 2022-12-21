from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Voditelj(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    email = models.EmailField()
    adresa = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    
    def __str__(self):
        return self.prezime

class Racunalo(models.Model):
    id_racunala=models.IntegerField(primary_key=True, default=1)
    #id_racunala=models.CharField(primary_key=True, default='#1')
    marka = models.CharField(max_length=10)
    tip = models.CharField(max_length=20)
    operacijski_sustav = models.CharField(max_length=20)
    mreza = models.BooleanField(default=True)
    
    def __str__(self):
        return "{}, {}".format(self.marka, self.tip)
            
class Prostorija(models.Model):
    broj_prostorije = models.IntegerField(default=1)
    kat = models.IntegerField(default=0)
    naziv_prostorije = models.TextField(default="Prazna dvorana")
    glavno_racunalo = models.OneToOneField(Racunalo, on_delete=models.CASCADE, default=404)
    
    def __str__(self):
        return "{}. kat, Dvorana {}".format(self.kat,self.broj_prostorije)

class Aktivnost(models.Model):
    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    vrijeme_pocetka = models.DateTimeField('Datum početka')
    vrijeme_zavrsetka = models.DateTimeField('Datum planiranog završetka')
    voditelji_aktivnosti = models.ManyToManyField(Voditelj)
    prostorija_izvodjenja = models.ForeignKey(Prostorija, on_delete=models.CASCADE)

    def __str__(self):
         return self.naziv


    
    