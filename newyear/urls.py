from django.urls import path

# Create your urls here.
from . import views




urlpatterns = [
    path('',views.index, name="index"),
  
    
 ]
