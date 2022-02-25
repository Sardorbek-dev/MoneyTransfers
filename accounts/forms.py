from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from articles.models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age',) # Bio was deleted, because user can create a bio, after creating a profile 

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
