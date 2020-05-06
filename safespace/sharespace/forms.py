from django import forms
from .models import Room, Post


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #exclude = ['author', 'updated', 'created']
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'placeholder': 'Say something...'
            }),
        }


class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos:')
