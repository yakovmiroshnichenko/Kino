from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .forms import *


def create_film(request):
    formset = modelformset_factory(Image, form=ImageGalleryForm, extra=0, can_delete=True)
    if request.method == 'POST':
        form = AddFilmForm(request.POST, request.FILES)
        gallery_formset = formset(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film')
    else:
        form = AddFilmForm()
        gallery_formset = formset()
    return render(request, 'admin/create_film.html', {'form': form, 'formset': gallery_formset})


def basic(request):
    return render(request, 'layout/basic.html', {})
