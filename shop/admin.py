from django.contrib import admin
from .models import Category, Product

#admin.site.register(Category)
#admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

