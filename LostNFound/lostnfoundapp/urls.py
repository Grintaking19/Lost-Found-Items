# import path from django.urls
from django.urls import path 
from . import views

urlpatterns = [
path('upload' , views.index , name = 'index')
]