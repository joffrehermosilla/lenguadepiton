from django.contrib import admin

from .models import Reconocimiento, Airport, Passenger

# Register your models here.

class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    
    
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights", )
    

admin.site.register(Airport)
admin.site.register(Reconocimiento, ReconocimientoAdmin)
admin.site.register(Passenger, PassengerAdmin)