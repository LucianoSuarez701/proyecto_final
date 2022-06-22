from django.contrib import admin
from app_product.models import Celulares, Heladeras, Televisores

# Register your models here.

@admin.register(Celulares)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'inches', "description", "SKU", "is_active"]


@admin.register(Heladeras)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'litters', "description", "SKU", "is_active"]

@admin.register(Televisores)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'inches', "description", "SKU", "is_active"]