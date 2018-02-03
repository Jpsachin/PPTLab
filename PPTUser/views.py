from django.shortcuts import render
from . import templates
def Index(request):   
   return render(request, 'index.html',)

# Create your views here.
