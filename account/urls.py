from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home),
    path('about', views.about),
    path('registration', views.registration),
    path('renewal', views.renewal),
    path('contact', views.contact),
]