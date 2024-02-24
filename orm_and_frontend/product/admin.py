from django.contrib import admin
from product.models import ProductTable,CartTable
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','sku','name','price','details','category','is_active','size','image']
    search_fields = ['sku']

admin.site.register(ProductTable,ProductAdmin)
admin.site.register(CartTable)