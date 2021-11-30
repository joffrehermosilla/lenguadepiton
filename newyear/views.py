import _datetime

now = _datetime.date.today()

from django.shortcuts import render

# Create your views here.

    
def index(request):
   
    return render(request, "newyear/index.html",{
         "newyear":  now.month ==1 and now.day == 1
    })