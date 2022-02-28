from django.contrib import admin
from .models import Transfer, TransferComment

# Create class
class CommentInLine(admin.TabularInline):
    model = TransferComment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


# Register your models here.
admin.site.register(Transfer, ArticleAdmin)
admin.site.register(TransferComment)
