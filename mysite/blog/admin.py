from django.contrib import admin
from .models import Post
from .models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created', 'title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
