from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.forms import fields
from articles.models import Profile

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lastname'}))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age','gender',) # Bio was deleted, because user can create a bio, after creating a profile
        widgets = {
            'age': forms.TextInput(attrs={'class': "form-control mb-3", 'placeholder': 'firstname'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', ) # Bio was deleted, because user can create a bio, after creating a profile

class EditProfilePage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'telegram_url', 'instagram_url', 'facebook_url', )
        widgets = {
            'bio': forms.TextInput(attrs={'class': "form-control mb-3"}),
            'telegram_url': forms.TextInput(attrs={'class': "form-control mb-3"}),
            'instagram_url': forms.TextInput(attrs={'class': "form-control mb-3"}),
            'facebook_url': forms.TextInput(attrs={'class': "form-control mb-3"}),
        }


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'user_image', 'telegram_url', 'instagram_url', 'facebook_url', )
        widgets = {
            'bio': forms.Textarea(attrs={'class': "form-control mb-3", 'placeholder': 'Bio'}),
            # 'user_image': forms.ImageField(),
            'telegram_url': forms.TextInput(attrs={'class': "form-control mb-3"}),
            'instagram_url': forms.TextInput(attrs={'class': "form-control mb-3"}),
            'facebook_url': forms.TextInput(attrs={'class': "form-control mb-3"}),
        }
