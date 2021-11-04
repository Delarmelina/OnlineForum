from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'keyWords', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'required': 'true', 'autofocus': 'true'}),
            'author': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'keyWords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords', 'required': 'true'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'required': 'true', 'rows': '15'}),
        }