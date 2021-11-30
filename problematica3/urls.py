from django.urls import path

# Create your urls here.
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path("<str:name>", views.greet, name='greet'),
    path("hugo",views.hugo, name="hugo"),
    path("gustavo", views.gustavo, name ='gustavo'),
    path("carlo", views.carlo, name='carlo'),
    path("joffre", views.joffre, name='joffre')
    
 ]

    
