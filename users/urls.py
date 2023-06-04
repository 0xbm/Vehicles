from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register_user/", views.register_user, name="register_user"),
    path("delete_user/", views.delete_user, name="delete_user"),
    path("login_user/", views.login_user, name="logins"),
]
