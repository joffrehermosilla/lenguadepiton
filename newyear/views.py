import _datetime

now = _datetime.date.today()

from django.shortcuts import render

# Create your views here.

    
def index(request):
   #now = datetime.datetime.now()
    return render(request, "newyear/index.html",{
         "newyear":  now.month ==11 and now.day == 30
    })