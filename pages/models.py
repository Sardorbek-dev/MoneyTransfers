from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class ContactUs(models.Model):
    select_salutation = (
        ('mr', 'Mr.'),
        ('ms', 'Ms.'),
        ('mrs', 'Mrs.'),
        ('dr.', 'Dr.'),
        ('prof', 'Prof.'),
    )
    salutation = models.CharField(max_length=50, choices=select_salutation, verbose_name="Mr. or Ms. ?")
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    subject =models.CharField(max_length=100)
    content = RichTextField(verbose_name="Write your message...")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname)

    def get_absolute_url(self):
        return reverse('home')
