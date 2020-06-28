from django.db import models

from datetime import date

from producten.models import Product


# Create your models here.
class ManueleCorrectie(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    bedrag = models.DecimalField(max_digits=9, decimal_places=2)
    TOEPASSINGSKEUZES = [
        ("AANKOOP", "Aankoopbedrag"),
        ("VERKOOP", "Verkoopbedrag")
    ]
    toepassen_op = models.CharField(
        max_length=7,
        choices=TOEPASSINGSKEUZES,
        default="AANKOOP")

    def __str__(self):
        str(self.datum) + " - " + self.product.ticker


class Schikking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    bedrag = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        str(self.datum) + " - " + self.product.ticker


class WinstDeelname(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    aantal = models.IntegerField()
    bedrag = models.DecimalField(max_digits=9, decimal_places=5)

    def __str__(self):
        str(self.datum) + " - " + self.product.ticker