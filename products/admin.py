from django.contrib import admin

# Register your models here.
from products.models import Basket, Product, ProductCategory

# admin.site.register(Product)
# admin.site.register(Basket)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')
    fields = ('image', 'description', 'name', ('quantity', 'price'), 'category', )
    search_fields = ('name', )
    ordering = ('-name', 'price')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp', )
    extra = 0
