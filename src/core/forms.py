from django import forms
from src.cinema.models import *
from src.gallery_seo.models import *


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'description', 'main_image', 'trailer_url')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
                   'main_image': forms.FileInput(attrs={'class': 'custom-fileInput-image'}),
                   'gallery': forms.FileInput(attrs={'class': 'custom-fileInput-image'}),
                   'trailer_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка на видео в '
                                                                                                'YouTube'}),
                   }


class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {}
