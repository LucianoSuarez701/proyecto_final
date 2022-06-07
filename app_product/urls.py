from django.urls import path

from app_product.views import List_products, Detail_Celulares, Detail_Heladeras, Detail_Televisores

urlpatterns =[
        path('', List_products.as_view(), name = 'list_products'),
        path('heladeras/', Detail_Heladeras.as_view(), name = 'detail_heladeras'),
        path('celulares/', Detail_Celulares.as_view(), name = 'detail_celulares'),
        
]