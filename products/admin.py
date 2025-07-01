from django.contrib import admin

from products.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
