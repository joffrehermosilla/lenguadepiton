from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Reconocimiento, Passenger



#######################################harvard ejemplo









#############################################################




# Create your views here.
def index(request):
    return render(request,"index6.html",{
    
        "reconocimientox": Reconocimiento.objects.all()
        
    
    })
      
def reconoxco(request, reconoxco_id):   
    reconoxco = Reconocimiento.objects.get(pk=reconoxco_id)
    return render(request, "reconoxco.html" ,{
         "reconoxco": reconoxco, 
        "passengers": reconoxco.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=reconoxco).all()
        })
    
    
    
def book (request, reconoxco_id): 
    if request.method == "POST":
        reconoxco = Reconocimiento.objects.get(pk=reconoxco_id)
        passenger = Passenger.objects.get(pk=iterable(request.POST["passenger"]))
        passenger.reconocimientox.add(reconoxco)
        return HttpResponseRedirect(reverse("reconoxco", args=(reconoxco.id) ))
    
    
    
    
    
    

def hugo(request):
    return HttpResponse("Hello, Hugo!")

def gustavo(request):
    return HttpResponse("Hello, Gustavo!")

def carlo(request):
    return HttpResponse("Hello, Carlo!")

def joffre(request):
    return HttpResponse("Hello, Joffre!")

def greet(request, name):
   # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "greet.html", {
    
       "name":name.capitalize()
        
    })


#######################################view pytorch tutoeial



























