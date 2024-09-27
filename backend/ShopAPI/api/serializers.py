from rest_framework import serializers
from django.contrib.auth.models import User



class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()
    

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, read_only=True)
    id = serializers.IntegerField(read_only=True)
    has_perms = serializers.BooleanField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'id', 'has_perms', 'user_product')
    
    
    def get_user_product(self,obj):
        # user.product_set.all() : faire la relation inverse
        user = obj
        request = self.context.get('request')
        product = user.product_set.all()
        return ProductInlineSerializer(product, many=True, context={'request':request}).data