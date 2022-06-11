from django import forms
from .models import Post, Category

# choices = [('coding', 'coding'), ('Sport', 'Sport'), ('Poetry', 'Poetry'), ('lifestyle', 'lifestyle')]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  # For a while a just stay it here
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})

        }

