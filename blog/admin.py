
from django.contrib import admin
from .models import BlogPost, Comment, Like, Profile,Post

admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Post)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published', 'created_at')
    list_filter = ('published',)

admin.site.register(BlogPost, BlogPostAdmin)
