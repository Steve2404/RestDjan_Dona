from django.urls import path

from .views import DetailProductView, CreateProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    path('<int:pk>/', DetailProductView.as_view()),
    path('<int:pk>/update', UpdateProductView.as_view()),
    path('<int:pk>/delete', DeleteProductView.as_view()),
    path('create/', CreateProductView.as_view()),
    
]