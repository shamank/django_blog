from django.contrib import admin

# Register your models here.
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'image', 'content', 'category', 'created_at', 'update_at', 'created_by', 'update_by', 'slug'
        )
    list_display_links = ('id', 'title', 'category')
    search_fields = ('id', 'title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)