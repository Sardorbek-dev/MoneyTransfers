from django.db import models
from django import forms
from .models import TransferComment, Transfer

class TransferForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Transfer nomi', 'class': "form-control my-1"}))
    # moneyCurrency = forms.ChoiceField(label="moneyCurrency1")
    # transferArt = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'pleaceholder': 'Write comment'}))
    # whichLocation = forms.CharField(label="whichLocation1", widget=forms.Textarea(attrs={'class': 'form-control', 'pleaceholder': 'Write comment'}))

    class Meta:
        model = Transfer
        fields = ('title', 'description', 'location', 'moneyCurrency', 'transferArt', 'whichLocation', 'price',  )
        # widgets = {
        #     'location': forms.ChoiceField(attrs={'class': "form-control"}),
        # }

class TransferCommentForm(forms.ModelForm):
    transfer_comment = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'pleaceholder': 'Write comment'}))
    class Meta:
        model = TransferComment
        fields = ('transfer_comment', )
        widgets = {
            'transfer_comment': forms.TextInput(attrs={'class': "form-control mb-3", 'placeholder': 'comment'}),
        }
