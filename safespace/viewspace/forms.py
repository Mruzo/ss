from django import forms
from .models import Photos

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )
