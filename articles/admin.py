from django.contrib import admin
from .models import Article, Comment, Category, Profile

# Create class
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class TransferAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

# Register your models here.
admin.site.register(Article, TransferAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Profile)