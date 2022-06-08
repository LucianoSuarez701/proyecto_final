from django.urls import path

from app_product.views import List_products

from app_product.views import mostrar_heladeras, mostrar_celulares, mostrar_televisores

urlpatterns =[
         #path('', List_products.as_view(), name = 'list_products'),

        # path("heladeras/", mostrar_heladeras, name = "heladeras"),
        # path("celulares/", mostrar_celulares, name = "celulares"),
        # path("televisores/", mostrar_televisores, name = "televisores"),
        
]