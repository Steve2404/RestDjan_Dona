from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def api_view(request, *args, **kwargs):
    # request instance de HttpRequest
    print(request.body) # retourne un byte string
   
    data = json.loads(request.body)
    pre_data = json.dumps(data)
    print(pre_data)
    print(data)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post_data'] = dict(request.POST)
    
    print(request.headers)
    
    return JsonResponse(data)