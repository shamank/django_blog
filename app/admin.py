from django.contrib import admin
from django import forms


# Register your models here.
from .models import Post, Category, Tag

from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = (
        'id', 'title', 'description', 'image', 'category', 'created_at', 'update_at', 'created_by', 'update_by', 'slug'
        )
    list_display_links = ('id', 'title', 'category')
    search_fields = ('id', 'title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'slug')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'slug')  


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)