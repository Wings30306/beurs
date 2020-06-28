from django.contrib import admin
from .models import Aankoop, Verkoop, Dividend

# Register your models here.
admin.site.register(Aankoop)
admin.site.register(Verkoop)
admin.site.register(Dividend)