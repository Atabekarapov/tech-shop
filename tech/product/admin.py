from django.contrib import admin

from .models import Category, Product, ProductImage, Comment


class ImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ['image']


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine
    ]
    list_display = ('uuid', 'title', 'price')
    list_display_links = ('uuid', 'title')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
# admin.site.register(ProductImage)