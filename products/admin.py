from django.contrib import admin
from .models import Poster, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        
        'name',
    )


admin.site.register(Poster, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
