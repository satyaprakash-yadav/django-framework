from django.contrib import admin
from . models import CategoryModel, ImageModel

# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Title']

@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Category', 'Image', 'Description']
