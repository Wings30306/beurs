from django.db import models
from products.models import Product

# Create your models here.
class Aankoop(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    aantal = models.IntegerField()
    koers = models.DecimalField(max_digits=9, decimal_places=5)


class Verkoop(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    aantal = models.IntegerField()
    koers = models.DecimalField(max_digits=9, decimal_places=5)


class Dividend(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    datum = models.DateField(default=date.today)
    bedrag = models.DecimalField(max_digits=9, decimal_places=2)


class Correctie(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    bedrag = models.DecimalField(max_digits=9, decimal_places=2)