from django.shortcuts import render
from django.http import HttpResponse

from unicodedata import name #que es esto?

from django.views.generic import ListView # esto es de la nueva clase para mostrar una lista de productos

from app_product.models import Celulares, Heladeras, Televisores
from app_product.forms import Celulares_form, Heladeras_form, Televisores_form

# Create your views here.
def products(request):
    print(request.method)
    productos = Celulares.objects.all()
    context = {'celulares':Celulares}
    return render(request, 'celulares.html', context=context)

def products(request):
    print(request.method)
    productos = Heladeras.objects.all()
    context = {'heladeras': Heladeras}
    return render(request, 'heladeras.html', context=context)

def products(request):
    print(request.method)
    productos = Televisores.objects.all()
    context = {'televisores': Televisores}
    return render(request, 'televisores.html', context=context)    

class List_products(ListView):
    model = Heladeras
    template_name= 'productos.html'
    queryset = Heladeras.objects.filter(is_active = True)    