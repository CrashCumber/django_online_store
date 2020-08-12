from django.contrib import admin
from .models import Product, Brand, Banner


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'definition')
    exclude = ('picture',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'definition')
