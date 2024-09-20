from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers


@api_view(['GET', 'POST'])
def api_view(request):
    if query := Product.objects.all().order_by('?').first():
        #data = model_to_dict(query, fields=['name', 'content', 'price', 'get_discount'])
        data = ProductSerializers(query).data
    else:
        data = {}
    return Response(data)