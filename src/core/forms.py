from django import forms
from src.cinema.models import *


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'description', 'main_image', 'trailer_url')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
                   'main_image': forms.FileInput(attrs={'class': 'custom-fileInput-image'}),
                   'trailer_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка на видео в '
                                                                                                'YouTube'})
                   }
