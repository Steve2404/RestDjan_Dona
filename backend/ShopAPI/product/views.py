from .models import Product, TokenExtension

from rest_framework.response import Response
from .serializers import ProductSerializers
from rest_framework import generics, mixins, permissions, authentication
from api.mixins import StaffEditorPermissionMixins
from .authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Token
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta


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
 


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Authentification de l'utilisateur
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

       # Vérifier si un token existe déjà pour cet utilisateur
        token = Token.objects.filter(user=user).first()

        if token:
            # Vérifier si l'extension de token existe
            try:
                extension = token.extension
            except TokenExtension.DoesNotExist:
                # Si l'extension n'existe pas, la créer
                extension = TokenExtension.objects.create(token=token, expiry_date=timezone.now() + timedelta(days=1))
            
            # Vérifier si le token est expiré
            if extension.is_expired():
                # Si le token est expiré, le supprimer et en créer un nouveau
                token.delete()
                token = Token.objects.create(user=user)
                # Créer une nouvelle extension pour le nouveau token
                extension = TokenExtension.objects.create(token=token, expiry_date=timezone.now() + timedelta(days=1))
        else:
            # Si aucun token n'existe, en créer un nouveau
            token = Token.objects.create(user=user)
            # Créer une extension pour ce nouveau token
            extension = TokenExtension.objects.create(token=token, expiry_date=timezone.now() + timedelta(days=1))

        return Response({
            'token': token.key,
            'expiry_date': extension.expiry_date.isoformat(),
        })
       
class ProductMixinsViews(
        StaffEditorPermissionMixins,
        generics.GenericAPIView,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
 
    def perform_update(self, serializer): 
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None: 
            content = name    
        serializer.save(content=content)
        
    def perform_create(self, serializer):
        # email = serializer.validated_data.pop('email')
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

    
    