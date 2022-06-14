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
     heladeras = Heladeras.objects.all()                                
     context = {'heladeras':heladeras}
     return render(request, 'heladeras.html', context=context)


def mostrar_televisores(request):
     televisores = Televisores.objects.all()                                
     context = {'televisores':televisores}
     return render(request, 'televisores.html', context=context)

# def search_products(request):
#      products = [Heladeras.objects.filter(name__icontains=request.GET['search']), Televisores.objects.filter(name__icontains=request.GET['search']), Celulares.objects.filter(name__icontains=request.GET['search'])]
#      if products.exists():
#           context = {'products':}
#      else:
#           context = {'errors':'No se encontro el producto'}
#      return render(request, 'search-products.html', context = context)

def search_products(request):
     productoheladeras = Heladeras.objects.filter(name__icontains=request.get['search']),
     productocel = Celulares.objects.filter(name__icontains=request.get['search']),
     productotv = Televisores.objects.filter(name__icontains=request.get['search']),
     if productoheladeras.exists():
          context = {'productoheladeras': productoheladeras},
     elif productotv.exists():
          context = {'productotv': productotv},
     elif productocel.exists():
          context = {'productocel': productocel},
     else:
          context = {"errors": 'No se encuentra el producto'}
     return render(request, search_products.html, context=context)
