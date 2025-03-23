from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stats/<str:name>/", views.stats, name="stats"),
]