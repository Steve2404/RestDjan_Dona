from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import CustomAuthToken, DetailProductView, CreateProductView,\
ListProductView, UpdateProductView, DeleteProductView, ProductMixinsViews

urlpatterns = [
   # path('<int:pk>/', DetailProductView.as_view()),
   # path('<int:pk>/update', UpdateProductView.as_view()),
   # path('<int:pk>/delete', DeleteProductView.as_view()),
   # path('create/', CreateProductView.as_view()),
   # path('liste/', ListProductView.as_view()),
   # path('mixins/', ProductMixinsViews.as_view()),
    path('create/', ProductMixinsViews.as_view()),
    path('<int:pk>/detail', ProductMixinsViews.as_view(), name='product-detail'),
    path('<int:pk>/update', ProductMixinsViews.as_view()),
    path('<int:pk>/delete', ProductMixinsViews.as_view()),
    path('liste/', ProductMixinsViews.as_view()),
    path('auth/', CustomAuthToken.as_view())
    # path('auth/', obtain_auth_token)
    
    
    
]