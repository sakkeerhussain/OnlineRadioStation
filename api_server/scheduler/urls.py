from django.contrib import admin
from django.urls import path

from scheduler.views import NextMusicView

urlpatterns = [
    path('next/', NextMusicView.as_view()),
]
