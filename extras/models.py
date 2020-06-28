from django.db import models
from django.contrib.auth.models import User

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
         return self.user.username + " - " + self.product.ticker + " gecorrigeerd op " + self.datum.strftime("%Y-%m-%d")


class Schikking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    bedrag = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
         return self.user.username + " - Schikking van" + self.product.ticker + " ontvangen op " + self.datum.strftime("%Y-%m-%d")


class WinstDeelname(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    aantal = models.IntegerField()
    bedrag = models.DecimalField(max_digits=9, decimal_places=5)

    def __str__(self):
        return self.user.username + " - Deelname in the winst" + self.product.ticker + " ontvangen op " + self.datum.strftime("%Y-%m-%d")


class Splitsing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    factor = models.IntegerField()
    omgekeerde_splitsing = models.BooleanField()

    def __str__(self):
        return self.user.username + " - Aandelensplitsing van " + self.product.ticker + " uitgevoerd op " + self.datum.strftime("%Y-%m-%d")