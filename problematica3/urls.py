from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# Create your urls here.
from . import views


app_name ='Problematica3'

urlpatterns = [
    path('',views.index, name="index"),
    path("<str:name>", views.greet, name='greet'),
    path("hugo",views.hugo, name="hugo"),
    path("gustavo", views.gustavo, name ='gustavo'),
    path("carlo", views.carlo, name='carlo'),
    path("joffre", views.joffre, name='joffre')
    
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
