from django.contrib import admin
# Register your models here.
from products.models import ProductDetail, Products, OrderNow, It, Application


class ProductDetailInline(admin.StackedInline):
    model = ProductDetail


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDetailInline]
    list_display = ['service_rendered']
    list_filter = ['service_rendered']
    search_fields = ['service_rendered']


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['price']
    list_filter = ['price']
    search_fields = ['price']


admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(OrderNow)
admin.site.register(It)
admin.site.register(Application)
