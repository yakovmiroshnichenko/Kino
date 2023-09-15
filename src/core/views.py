from django.shortcuts import render


def film(request):
    return render(request, 'admin/create_film.html', {})


def basic(request):
    return render(request, 'layout/basic.html', {})
