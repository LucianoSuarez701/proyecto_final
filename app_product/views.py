from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from app_product.models import Celulares, Heladeras, Televisores
from django.views.generic import ListView, CreateView  # VISTAS GENERICAS DE DJANGO

# Create your views here.

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

def search_products(request):

     productoheladeras = Heladeras.objects.filter(name__icontains=request.GET['search'])
     productocel = Celulares.objects.filter(name__icontains=request.GET['search'])
     productotv = Televisores.objects.filter(name__icontains=request.GET['search'])
     print(2)

     if productoheladeras.exists():
         context = {'productoheladeras': productoheladeras}
         print (1)
     elif productotv.exists():
            context = {'productotv': productotv}
     elif productocel.exists():
            context = {'productocel': productocel}
     else:
          context = {"errors": 'No se encuentra el producto'}
     return render(request, "search_product.html", context = context)

def detalle_celulares(request, pk):    
     detalle_celulares = Celulares.objects.get(id=pk)                                
     context = {'detalle_celulares':detalle_celulares}
     return render(request, 'detalle_celulares.html', context=context) 

def detalle_heladeras(request, pk):    
     detalle_heladeras = Heladeras.objects.get(id=pk)                                
     context = {'detalle_heladeras':detalle_heladeras}
     return render(request, 'detalle_heladeras.html', context=context) 

def detalle_televisores(request, pk):    
     detalle_televisores = Televisores.objects.get(id=pk)                                
     context = {'detalle_televisores':detalle_televisores}
     return render(request, 'detalle_televisores.html', context=context)      

class List_products(ListView):
    model = Heladeras, Celulares, Televisores 
    template_name= 'productos.html'
    
class Crear_celular(CreateView):
    model = Celulares
    template_name = 'crear_celular.html'
    fields = '__all__'    

    def get_success_url(self):
        return reverse('celulares')   

class Crear_heladera(CreateView):
    model = Heladeras
    template_name = 'crear_heladera.html'
    fields = '__all__'    

    def get_success_url(self):
        return reverse('heladeras')    

class Crear_televisor(CreateView):
    model = Televisores
    template_name = 'crear_televisor.html'
    fields = '__all__'    

    def get_success_url(self):
        return reverse('televisores') 


       