from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'created_at', 'views', 'category', 'get_photo']
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    form = PostAdminForm
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    save_on_top = True
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'author', 'content', 'created_at', 'views',  'photo', 'get_photo', 'category', 'tags')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width = "50">')
        return ' - '

    get_photo.short_description = 'Photo'


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Post, PostAdmin)

