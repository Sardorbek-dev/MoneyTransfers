from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    #gender = models.PositiveIntegerField(null=True, blank=True)
    gender_os_choice = (
        ('male', 'Man'),
        ('female', 'Woman'),
    )
    gender = models.CharField(max_length=100, choices=gender_os_choice)
    # gender = forms.ChoiceField(choices=gender_os_choice, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))