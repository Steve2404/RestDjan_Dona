from rest_framework import serializers
from rest_framework.reverse import reverse
from .views import Product
from .validators import validators_unique_product_name
from api.serializers import UserPublicSerializer

class ProductSerializers(serializers.ModelSerializer):
    
    my_discounts = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validators_unique_product_name])
    
    # serializer cette attribut a partie d un autre serializer
    # owner = UserPublicSerializer(source='user', read_only=True)
    
    class Meta:
        model = Product
        fields = ('email', 'url', 'pk', 'name', 'content', 'price', 'my_discounts')
     
    

     
    def create(self, validated_data):
        email = validated_data.pop('email')
        #return Product.objects.create(**validate_data)
        obj = super().create(validated_data)
        return obj
        
    def update (self, instance, validated_data):
        #instance.name = validated_data.get('name')
        # return instance
        return super().update(instance, validated_data)
        
    def get_my_discounts(self, obj):
        # sourcery skip: assign-if-exp, reintroduce-else
        if not hasattr(obj, 'id'): 
           return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount() 
    
   