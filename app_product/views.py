from django.shortcuts import render
from django.http import HttpResponse
from unicodedata import name #que es esto?
from app_product.models import Celulares, Heladeras, Televisores
# from app_product.forms import Celulares_form, Heladeras_form, Televisores_form # FORMULARIOS VIEJOS, AHORA USAMOS LAS VISTAS GENERICAS DE DJANGO
from django.views.generic import ListView, DetailView, CreateView # VISTAS GENERICAS DE DJANGO

# Create your views here.


class List_products(ListView):
    model = Heladeras, Celulares, Televisores 
    template_name= 'productos.html'

class Detail_Heladeras(DetailView):
    model = Heladeras
    template_name= 'heladeras.html'
    
class Detail_Celulares(DetailView):
    model = Celulares
    template_name= 'celulares.html'
    
class Detail_Televisores(DetailView):
    model = Televisores
    template_name= 'televisores.html'

# def products(request):
#     print(request.method)
#     productos = Celulares.objects.all()
#     context = {'celulares':Celulares}
#     return render(request, 'celulares.html', context=context)

# def products(request):
#     print(request.method)
#     productos = Heladeras.objects.all()
#     context = {'heladeras': Heladeras}
#     return render(request, 'heladeras.html', context=context)

# def products(request):
#     print(request.method)
#     productos = Televisores.objects.all()
#     context = {'televisores': Televisores}
#     return render(request, 'televisores.html', context=context)    