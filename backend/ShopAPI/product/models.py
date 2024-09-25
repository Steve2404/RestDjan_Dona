from django.db import models
from rest_framework.authtoken.models import Token 
from django.utils import timezone
from datetime import timedelta


class TokenExtension(models.Model):
    token = models.OneToOneField(Token, on_delete=models.CASCADE, related_name='extension')
    expiry_date = models.DateTimeField(default=timezone.now() + timedelta(days=1))

    def is_expired(self):
        if timezone.now() < self.expiry_date:
            remaining_time = self.expiry_date - timezone.now()
            remaining_minutes = remaining_time.total_seconds() / 60  
            print(f"Il te reste encore: {remaining_minutes:.2f} minutes")
            return False
        print("Depasser")
        return True


class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def get_discount(self):
        return "%.2f"%(float(self.price) * 0.5)
