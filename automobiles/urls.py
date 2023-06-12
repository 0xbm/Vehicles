from django.urls import path
from . import views

app_name = "automobiles"
urlpatterns = [
    path("", views.home, name="home"),
    path("add_vehicle/", views.add_vehicle, name="add_vehicle"),
    # path("contact/", views.contact, name="contact"), # to jest contact z html form (ladny)
    path("all_vehicles/", views.all_vehicles, name="all_vehicles"),
    path("list_vehicles/", views.list_vehicles, name="list_vehicles"),
    path("show_vehicle/<vehicle_id>", views.show_vehicle, name="show_vehicle"),
    path("search_vehicles/", views.search_vehicles, name="search_vehicles"),
    path("update_vehicle/<vehicle_id>", views.update_vehicle, name="update_vehicle"),

]
