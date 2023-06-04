from django.urls import path
from . import views

app_name = "automobiles"
urlpatterns = [
    path("", views.home, name="home"),
    path("add_vehicle/", views.add_vehicle, name="add_vehicle"),
    # path("contact/", views.contact, name="contact"), # to jest contact z html form (ladny)
    path("list_vehicles/", views.list_vehicles, name="list_vehicles"),
]
