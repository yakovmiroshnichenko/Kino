from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings
from src.core.views import film


urlpatterns = [
    path('', film, name='film'),
]
