from django.urls import path
from . import views

urlpatterns = [ 
    path('main', views.home),
    path('about', views.about),
    path('registration', views.registration),
    path('renewal', views.renewal),
    path('contact', views.contact),
    path('faq', views.faq),
    path('login', views.login),
]