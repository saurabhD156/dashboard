from django.contrib import admin
from .models import Image, MetaData, Category, Tag, Post

# Register your models here.

admin.site.register(Image)
admin.site.register(MetaData)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)