from django.http import HttpResponse
from django.shortcuts import render




#######################################harvard ejemplo









#############################################################




# Create your views here.
def index(request):
    return render(request,"index.html")

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

























