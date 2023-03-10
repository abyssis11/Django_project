import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Racunalo, Prostorija, Voditelj, Aktivnost
from main.factory import (
    ProstorijaFactory,
    RacunaloFactory,
    VoditeljFactory,
    AktivnostFactory
)

NUM_RACUNALA = 140
NUM_PROSTORIJA = 140
NUM_VODITELJA = 400
NUM_AKTIVNOSTI = 550
# Max voditelja aktivnosti
NUM_VODITELJA_AKTIVNOSTI = 3

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Voditelj,Racunalo, Prostorija, Aktivnost]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        voditelji = []
        for _ in range(NUM_RACUNALA):
            racunalo = RacunaloFactory()

        for _ in range(NUM_PROSTORIJA):
            prostorija = ProstorijaFactory()
        
        for _ in range(NUM_VODITELJA):
             voditelj = VoditeljFactory()
             voditelji.append(voditelj)

        for _ in range(NUM_AKTIVNOSTI):
            aktivnost = AktivnostFactory()

            # za many-to-many vezu
            va = random.choices(
                voditelji,
                k = NUM_VODITELJA_AKTIVNOSTI
            )
            aktivnost.voditelji_aktivnosti.add(*va)