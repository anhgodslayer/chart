from django.shortcuts import render
from .models import show
from django.db import connection
# Create your views here.
def index(request):
    data = "Current Data"
    zoneH=show.objects.all().count()
    context= {
        "data": data,
        "zoneH": zoneH,
    }
   
    return render(request, 'chartapp/index.html', context)