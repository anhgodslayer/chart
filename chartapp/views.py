from django.shortcuts import render

# Create your views here.
def index(request):
    data = "Current Data"

    context= {
        "data": data
    }
    return render(request, 'chartapp/index.html', context)