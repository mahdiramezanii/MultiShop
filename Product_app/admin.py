from django.contrib import admin
from .models import Category,Product,Size,Color,ProductImageGallery

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductImageGallery)
