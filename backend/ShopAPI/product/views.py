from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers


@api_view(['GET', 'POST'])
def api_view(request):  # sourcery skip: assign-if-exp, reintroduce-else
    
    
    serializer = ProductSerializers(data=request.data)
    # print(f"data: {serializer}")
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'datail': 'Invalid data'})
  