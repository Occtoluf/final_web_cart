from django.contrib import admin

from .models import Brand_s
from .models import Product_s

class Brand_sAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name','description')
    prepopulated_fields ={"slug": ("name",)}







class Product_sAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'slug', 'quantity' )
    list_display_links = ('id', 'name')
    search_fields = ('name','description')
    prepopulated_fields ={"slug": ("name",)}


admin.site.register(Brand_s, Brand_sAdmin)
admin.site.register(Product_s, Product_sAdmin)