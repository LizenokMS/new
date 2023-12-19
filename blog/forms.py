from django.forms import ModelForm,TextInput,Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название',
                'class': 'form-control'
            }),
            'post': Textarea(attrs={
                'placeholder': 'Описание',
                'class': 'form-control'
            })
            }