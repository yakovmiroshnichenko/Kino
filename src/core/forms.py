from django import forms
from src.cinema.models import *
from src.gallery_seo.models import *


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'description', 'main_image', 'trailer_url', 'type_2D', 'type_3D', 'type_IMAX')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
                   'main_image': forms.FileInput(attrs={'class': 'custom-fileInput-image'}),
                   'gallery': forms.FileInput(attrs={'class': 'custom-fileInput-image'}),
                   'trailer_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка на видео в '
                                                                                                'YouTube'}),
                   'type_2D': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   'type_3D': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   'type_IMAX': forms.CheckboxInput(attrs={'class': 'form-check-input'})
                   }


class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {}
