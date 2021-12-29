from django.urls import path

from . import views 

urlpatterns = [
    
    path("", views.index, name="index5"),
     path("<int:flight_id>", views.flight, name="flight")
    
    
]