from django.urls import path

from app_product.views import List_products

urlpatterns =[
        path('', List_products.as_view(), name = 'list_products'),
]