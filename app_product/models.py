from django.db import models

# Create your models here.
class Celulares(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    inches = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    
    
class Heladeras(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    litters = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    
    
class Televisores(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    inches = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    