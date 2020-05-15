from django import forms
from .models import Room, Post


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'status', 'room_number', 'nobeds', 'room_type', )


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
