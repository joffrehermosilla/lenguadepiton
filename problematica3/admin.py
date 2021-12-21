from django.contrib import admin

from .models import Reconocimiento, Airport, Passenger

# Register your models here.

admin.site.register(Airport)
admin.site.register(Reconocimiento)
admin.site.register(Passenger)