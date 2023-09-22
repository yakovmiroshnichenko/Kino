from django.shortcuts import render, redirect
from .forms import *


def create_film(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film')
    else:
        form = AddFilmForm()
    return render(request, 'admin/create_film.html', {'form': form})


def basic(request):
    return render(request, 'layout/basic.html', {})
