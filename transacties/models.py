from django.db import models
from django.contrib.auth.models import User

from datetime import date

from producten.models import Product


# Create your models here.
class Aankoop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    aantal = models.IntegerField()
    koers = models.DecimalField(max_digits=9, decimal_places=5)

    def __str__(self):
        return self.user.username + " - " + self.product.ticker + " aangekocht op " + self.datum.strftime("%Y-%m-%d")


class Verkoop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    aantal = models.IntegerField()
    koers = models.DecimalField(max_digits=9, decimal_places=5)

    def __str__(self):
         return self.user.username + " - " + self.product.ticker + " verkocht op " + self.datum.strftime("%Y-%m-%d")


class Dividend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    bedrag = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.user.username + " - dividend van " + self.product.ticker + " ontvangen op " + self.datum.strftime("%Y-%m-%d")
