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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from proyecto_final.views import index
from django.conf import  settings
from django.conf.urls.static import static

from app_product.views import search_products 
from app_product.views import Crear_celular, Crear_heladera, Crear_televisor
from app_product.views import mostrar_heladeras,mostrar_celulares, mostrar_televisores
from app_product.views import detalle_celulares, detalle_heladeras, detalle_televisores
from app_product.views import eliminar_celular, eliminar_heladera, eliminar_televisor
from app_product.views import Editar_celular, Editar_heladera, Editar_televisor
from proyecto_final.views import login_view, register_view, logout_view, contact, leandro, luciano, about, lautaro

#from app_product.views import List_products
#from django.urls import include
urlpatterns = [

    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    
    path("search_product/", search_products, name = "search_products"),

    path("heladeras/", mostrar_heladeras, name = "heladeras"),
    path("celulares/", mostrar_celulares, name = "celulares"),
    path("televisores/", mostrar_televisores, name = "televisores"),
    

    path("detalle_celulares/<int:pk>/", detalle_celulares, name = "detalle_celulares"),
    path("detalle_heladeras/<int:pk>/", detalle_heladeras, name = "detalle_heladeras"),
    path("detalle_televisores/<int:pk>/", detalle_televisores, name = "detalle_televisores"), 

    path('crear_celular/', Crear_celular.as_view(), name = 'crear_celular'),
    path('crear_heladera/', Crear_heladera.as_view(), name = 'crear_heladera'),
    path('crear_televisor/', Crear_televisor.as_view(), name = 'crear_televisor'),

    path('editar_celular/<int:pk>/', Editar_celular.as_view(), name = 'editar_celular'),
    path('editar_heladera/<int:pk>/', Editar_heladera.as_view(), name = 'editar_heladera'),
    path('editar_televisor/<int:pk>/', Editar_televisor.as_view(), name = 'editar_televisor'),

    path('eliminar_celular/<int:pk>/', eliminar_celular, name = 'eliminar_celular'),
    path('eliminar_heladera/<int:pk>/', eliminar_heladera, name = 'eliminar_heladera'),
    path('eliminar_televisor/<int:pk>/', eliminar_televisor, name = 'eliminar_televisor'),
    
    
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    
    path('contact/', contact, name = 'contacto'),
    path('leandro/', leandro, name = 'leandro'),
    path('luciano/', luciano, name = 'luciano'),
    path('lautaro/', lautaro, name = 'lautaro'),
    path('about/', about, name = 'about'),
    
    # path('app_product/', include('app_product.urls')), 
    # path('', List_products.as_view(), name = 'list_products'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, Document_root=settings.MEDIA_ROOT)
