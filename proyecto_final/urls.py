"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_product.views import Crear_celular, Crear_heladera, Crear_televisor
from app_product.views import detalles_celulares

from proyecto_final.views import index
from app_product.views import mostrar_heladeras,mostrar_celulares, mostrar_televisores, search_products 

from app_product.views import List_products

urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    # path('app_product/', include('app_product.urls')), 
    # path('', List_products.as_view(), name = 'list_products'),
    path("heladeras/", mostrar_heladeras, name = "heladeras"),
    path("celulares/", mostrar_celulares, name = "celulares"),
    path("televisores/", mostrar_televisores, name = "televisores"),
    path("search_product/", search_products, name = "search_products"),

    path("detalles_celulares/", detalles_celulares, name = "detalles_celulares"),

    path('crear_celular/', Crear_celular.as_view(), name = 'crear_celular'),
    path('crear_heladera/', Crear_heladera.as_view(), name = 'crear_heladera'),
    path('crear_televisor/', Crear_televisor.as_view(), name = 'crear_televisor'),
    
]


