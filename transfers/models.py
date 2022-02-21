from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class Transfer(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    price = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('transfer_detail', args=[str(self.id)])
