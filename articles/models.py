from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime, date
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_new')

class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    user_image = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    telegram_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)
        
    def get_absolute_url(self):
        return reverse('home')

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, default='coding')
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    ) # ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(get_user_model(), related_name='blog_articles', blank=True)

    def get_likes(self):
        return self

    def total_likes(self):
        return self.likes.count() # just count all likes

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')