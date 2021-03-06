from django import forms
from .models import Comment, Article, Category

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'pleaceholder': 'Write text'}))
    class Meta:
        model = Comment
        fields = ('comment', )
        widgets = {
            'comment': forms.TextInput(attrs={'class': "form-control mb-3", 'placeholder': 'comment'}),
        }


choices_category = Category.objects.all().values_list('name', 'name') #name is same name with name in Category (name = models.CharField(max_length=200))

choices_category_list = []

for item in choices_category:
    choices_category_list.append(item)

# choices_category = [
#     ('coding', 'Coding'),
#     ('sport', 'Sport'),
#     ('education', 'Education'),
# ]

# class AddArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ('title', 'summary', 'category', 'body',)
#         widgets = {
#             'title': forms.TextInput(attrs={'class': "form-control mb-3", 'placeholder': 'Title'}),
#             'summary': forms.TextInput(attrs={'class': "form-control mb-3"}),
#             'category': forms.Select(choices=choices_category_list, attrs={'class': "form-control mb-3"}),
#             'body': forms.Textarea(attrs={'class': "form-control mb-3"}),
#         }

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'summary', 'category', 'body', 'photo',)
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control mb-3", 'placeholder': 'Title'}),
            'summary': forms.TextInput(attrs={'class': "form-control mb-3"}),
            'category': forms.Select(choices=choices_category_list, attrs={'class': "form-control mb-3"}),
            'body': forms.Textarea(attrs={'class': "form-control mb-3"}),
        }

