from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Celulares(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    inches = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    image= models.ImageField(upload_to="celulares", blank=True, null=True)
    
class Heladeras(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    litters = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    image= models.ImageField(upload_to="heladeras", blank=True, null=True)
    
class Televisores(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    inches = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    