from django.urls import path
from . import views

app_name = "automobiles"
urlpatterns = [
    path("", views.index, name="index"),
]
