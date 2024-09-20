from django.urls import path

from .views import DetailApiView, CreateApiView

urlpatterns = [
    path('<int:pk>/', DetailApiView.as_view()),
    path('create/', CreateApiView.as_view()),
    
]