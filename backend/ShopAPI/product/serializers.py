from rest_framework import serializers
from .views import Product

class ProductSerializers(serializers.ModelSerializer):
    
    my_discounts = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ('pk', 'name', 'content', 'price', 'my_discounts')
        
    def get_my_discounts(self, obj):
        # sourcery skip: assign-if-exp, reintroduce-else
        if not hasattr(obj, 'id'): 
           return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount() 