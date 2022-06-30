from django import forms
from app_product.models import Celulares, Heladeras, Televisores

class Celulares_form(forms.ModelForm):
    class Meta:
        model = Celulares
        fields = '__all__'
        
class Heladeras_form(forms.ModelForm):
    class Meta:
        model = Heladeras
        fields = '__all__'
        
class Televisores_form(forms.ModelForm):
    class Meta:
        model = Televisores
        fields = '__all__'


class Crear_celulares_form(forms.ModelForm):
    class Meta:
        model = Celulares
        fields = ["name","price","inches","description","SKU", "is_active","image"] 

class Crear_heladeras_form(forms.ModelForm):
    class Meta:
        model = Heladeras
        fields = ["name","price","litters","description","SKU", "is_active", "image"]         

class Crear_televisores_form(forms.ModelForm):
    class Meta:
        model = Televisores
        fields = ["name","price","inches","description","SKU", "is_active","image"]         