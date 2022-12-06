from django.contrib import admin

from main.models import Brand_s, Product_s, Position, Size


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('size', 'product', 'quantity')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', )


class Brand_sAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name','description')
    prepopulated_fields ={"slug": ("name",)}


class Product_sAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name','description')
    prepopulated_fields ={"slug": ("name",)}


admin.site.register(Brand_s, Brand_sAdmin)
admin.site.register(Product_s, Product_sAdmin)