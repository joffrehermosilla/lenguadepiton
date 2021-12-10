from django.contrib import admin

from .models import Reconocimiento, Airport

# Register your models here.

admin.site.register(Airport)
admin.site.register(Reconocimiento)