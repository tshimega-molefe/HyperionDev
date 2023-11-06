from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("store", views.store),
    path("hello", views.hello),
]
