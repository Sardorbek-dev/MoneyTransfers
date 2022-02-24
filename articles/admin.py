from django.contrib import admin
from .models import Article, Comment, Category

# Create class
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)