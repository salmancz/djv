import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'account/main.html')

def about(request):
    return render(request, 'account/about.html')
	
def registration(request):
	return render(request, 'account/registration.html')

def renewal(request):
    return render(request, 'account/renewal.html')
	
def contact(request):
    	return render(request, 'account/contact.html')
 
def faq(request):
	return render(request, 'account/faq.html')