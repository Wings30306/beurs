from django.db import models

# Create your models here.
class Type(models.Model):
    naam = models.CharField(max_length=15)
    taks = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.naam + " - " + str(self.taks) + "%"

class Product(models.Model):
    isin = models.CharField(max_length=12, unique=True)
    ticker = models.CharField(max_length=5, primary_key=True, unique=True)
    naam = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    met_dividend = models.BooleanField()

    def __str__(self):
        return self.ticker