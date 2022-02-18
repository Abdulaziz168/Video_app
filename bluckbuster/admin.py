from django.contrib import admin
from .models import Banner, Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'id', 'category', 'modified_date')
    search_fields = ['product_name', ]
    list_filter = ['category', 'modified_date']
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)

admin.site.register(Banner)
admin.site.register(Category)
