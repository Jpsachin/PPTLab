from django.shortcuts import render
from . import templates

def Index(request):   
   return render(request, 'index.html',)
  
def login(request):
    return render(request, 'login.html',)
def about(request):
    return render(request, 'about.html',)
	
def bestdeals(request):
    return render(request, 'best-deals.html',)
	
def events(request):
    return render(request, 'events.html',)
	
def services(request):
    return render(request, 'services.html',)
	
def specialoffers(request):
    return render(request, 'special-offers.html',)
	
def mail(request):
    return render(request, 'mail.html',)
	
def economics(request):
    return render(request, 'economics.html',)
	
def products(request):
    return render(request, 'products.html',)
	
def single(request):
    return render(request, 'single.html',)
	
def faqs(request):
    return render(request, 'faqs.html',)
	
def privacy(request):
    return render(request, 'privacy.html',)
	
# Create your views here.
