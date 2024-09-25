from django.contrib import admin
from .models import Product, TokenExtension


admin.site.register(Product)

@admin.register(TokenExtension)
class TokenExtensionAdmin(admin.ModelAdmin):
    list_display = ('token', 'expiry_date')