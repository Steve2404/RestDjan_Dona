from django.db import models
from rest_framework.authtoken.models import Token as Tokenn
from django.utils import timezone
from datetime import timedelta


class Token(Tokenn):
    expiry_date = models.DateTimeField(default=timezone.now() + timedelta(days=1)) 
    
    def is_expired(self):
        return timezone.now() > self.expiry_date


class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def get_discount(self):
        return "%.2f"%(float(self.price) * 0.5)
