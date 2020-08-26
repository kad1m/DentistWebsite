from django.contrib import admin
from .models import Post, Comment
from modeltranslation.admin import TranslationAdmin

# Register your models here.


class PostAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'meta', 'author', 'publish', 'status', 'image', 'description')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
