from rest_framework.routers import DefaultRouter
from product.viewsets import ProductViewSet

router = DefaultRouter()

router.register('product-b', ProductViewSet, basename='product-a')

urlpatterns = router.urls