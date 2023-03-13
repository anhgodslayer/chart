from django.urls import path
from . import views
urlpatterns =[ 
    path('chart/', views.index , name='chartapp'),
]