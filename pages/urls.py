from django.urls import path
from . import views # from all import views

urlpatterns = [
    path('', views.index, name = 'index'), # routing, '' is the root path, in flask we used '/' , views.index is referencing the method 'index' in the file 'views', name='index' is for easy referencing
    path('about', views.about, name = 'about')
]