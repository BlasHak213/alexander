from django.contrib import admin
from .models import Category, Post, PostCategory, Author


class PostAdmin(admin.ModelAdmin):
    def category(self, post):
        return ', '.join([category.name for category in post.postCategory.all()])

    list_display = ('id', 'title', 'text', 'categoryType', 'category')
    list_filter = ('title', 'categoryType', 'postCategory')
    search_fields = ('title', 'postCategory')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Author)