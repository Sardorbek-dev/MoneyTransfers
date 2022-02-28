from django import forms
from .models import TransferComment

class TransferCommentForm(forms.ModelForm):
    transfer_comment = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'pleaceholder': 'Write comment'}))
    class Meta:
        model = TransferComment
        fields = ('transfer_comment', )
        widgets = {
            'transfer_comment': forms.TextInput(attrs={'class': "form-control mb-3", 'placeholder': 'comment'}),
        }
