from django.contrib import admin
from .models import Image, MetaData, Category, Tag, Post

# Register Image Model
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'alt_tag', 'fileName', 'created_at', 'updated_at')
    search_fields = ('title', 'alt_tag', 'fileName')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Register MetaData Model
@admin.register(MetaData)
class MetaDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'keywords', 'index', 'created_at', 'updated_at')
    search_fields = ('title', 'keywords')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Register Category Model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'slug', 'description')
    search_fields = ('Name', 'slug')
    prepopulated_fields = {'slug': ('Name',)}  # Automatically populate slug based on the Name field

# Register Tag Model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # Automatically populate slug based on the name field

# Register Post Model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'published', 'views', 'created_at', 'updated_at')
    list_filter = ('published', 'created_at', 'updated_at', 'category')
    search_fields = ('title', 'user__username', 'category__Name', 'tags__name')
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate slug based on the title field
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)  # Allows better handling of many-to-many fields
