from .models import Product
from .serializers import ProductSerializers
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    