from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("opinion", views.opinion, name="opinion"),
    path("poll", views.poll, name="poll"),
]