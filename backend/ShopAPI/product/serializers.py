from rest_framework import serializers
from .views import Product

class ProductSerializers(serializers.ModelSerializer):
    my_discounts = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'content', 'price', 'my_discounts')
        
    def get_my_discounts(self, obj):
        return obj.get_discount() 