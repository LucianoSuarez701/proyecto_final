from django.urls import path

from app_product.views import List_products, Detail_Celulares, Detail_Heladeras, Detail_Televisores

from app_product.views import mostrar_heladeras

urlpatterns =[
        path('', List_products.as_view(), name = 'list_products'),

        path("heladeras/", mostrar_heladeras, name = "heladeras"),

        # path('heladeras/', Detail_Heladeras.as_view(), name = 'detail_heladeras'),
        # path('celulares/', Detail_Celulares.as_view(), name = 'detail_celulares'),
        # path('televisores/', Detail_Televisores.as_view(), name = 'detail_televisores'),
        
]