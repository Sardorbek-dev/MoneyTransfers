from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender_os_choice = (
        ('male', 'Man'),
        ('female', 'Woman'),
    )
    gender = models.CharField(max_length=100, choices=gender_os_choice)
      
    def __str__(self):
        return str(self.first_name)
    
    # to show first and lastname on search area
    def natural_key(self):
        return (self.first_name, self.last_name) 
