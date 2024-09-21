from .models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from rest_framework import generics



class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class CreateProductView(generics.CreateAPIView): 
     queryset = Product.objects.all()
     serializer_class = ProductSerializers
     def perform_create(self, serializer):
         name = serializer.validated_data.get('name')
         content = serializer.validate_data.get('content') or None
         if content is None:
             content = name
         
         serializer.save(content=content)

class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_update(self, serializer): 
        name = serializer.validated_data.get('name')
        content = serializer.validate_data.get('content') or None
        if content is None: 
            content = name
            
        serializer.save(content=content)
        
class DeleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers