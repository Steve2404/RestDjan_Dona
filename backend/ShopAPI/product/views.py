from .models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from rest_framework import generics, mixins, permissions, authentication
from .permissions import IsStaffPermission
from .authentication import TokenAuthentication



class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class CreateProductView(generics.ListCreateAPIView): 
     queryset = Product.objects.all()
     serializer_class = ProductSerializers
     def perform_create(self, serializer):
         name = serializer.validated_data.get('name')
         content = serializer.validated_data.get('content') or None
         if content is None:
             content = name
         
         serializer.save(content=content)

class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_update(self, serializer): 
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None: 
            content = name
            
        serializer.save(content=content)
        
class DeleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    def get_queryset(self):
        return super().get_queryset().filter(name__icontains='Banane')
    
class ProductMixinsViews(
        generics.GenericAPIView,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]
    authentication_classes = [authentication.SessionAuthentication, 
                              TokenAuthentication]
    def perform_update(self, serializer): 
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None: 
            content = name
            
        serializer.save(content=content)
    def perform_create(self, serializer):
         name = serializer.validated_data.get('name')
         content = serializer.validated_data.get('content') or None
         if content is None:
             content = name
         
         serializer.save(content=content)
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    
    