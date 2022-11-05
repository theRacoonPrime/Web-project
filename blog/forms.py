from django import forms
from .models import Post


# choices = [('coding', 'coding'), ('Sport', 'Sport'), ('Poetry', 'Poetry'), ('lifestyle', 'lifestyle')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Select(attrs={'class': 'form-control'})

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})

        }

