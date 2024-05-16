from django.contrib import admin

from catalog.models import Category, Product, Version
from blog.models import Publication

# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'publication_activ')
    list_filter = ('name',)
    search_fields = ('name', 'slug',)

@admin.register(Version)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'number', 'attribute_bul')
    list_filter = ('name',)
    search_fields = ('name',)