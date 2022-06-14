from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from unicodedata import name 
from app_product.models import Celulares, Heladeras, Televisores
# from app_product.forms import Celulares_form, Heladeras_form, Televisores_form # FORMULARIOS VIEJOS, AHORA USAMOS LAS VISTAS GENERICAS DE DJANGO
from django.views.generic import ListView # VISTAS GENERICAS DE DJANGO

# Create your views here.


class List_products(ListView):
    model = Heladeras, Celulares, Televisores 
    template_name= 'productos.html'

def mostrar_celulares(request):    
     celulares = Celulares.objects.all()                                
     context = {'celulares':celulares}
     return render(request, 'celulares.html', context=context)

def mostrar_heladeras(request):
     return render(request, 'heladeras.html')
 

def mostrar_televisores(request):
     return render(request, 'televisores.html')
   

