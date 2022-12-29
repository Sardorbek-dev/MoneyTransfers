from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    #salutation = forms.CharField(widget=forms.Select(attrs={'class': "form-control my-2"}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname', 'class': "form-control my-2"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname', 'class': "form-control my-2"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': "my-2 form-control new-Email"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': "form-control my-2"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': "form-control my-2"}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zip code', 'class': "form-control my-2"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'subject', 'class': "form-control my-2"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control my-2"}))

    class Meta:
        model = ContactUs
        fields = ['salutation', 'firstname', 'lastname', 'email', 'phone_number', 'address', 'zip_code', 'subject', 'content',]
