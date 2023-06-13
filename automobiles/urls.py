from django.urls import path
from . import views

app_name = "automobiles"
urlpatterns = [
    path("", views.home, name="home"),
    path("add_vehicle/", views.add_vehicle, name="add_vehicle"),
    path("all_vehicles/", views.all_vehicles, name="all_vehicles"),
    path("list_vehicles/", views.list_vehicles, name="list_vehicles"),
    path("show_vehicle/<vehicle_id>", views.show_vehicle, name="show_vehicle"),
    path("search_vehicles/", views.search_vehicles, name="search_vehicles"),
    path("update_vehicle/<vehicle_id>", views.update_vehicle, name="update_vehicle"),
    path("list_brand/", views.list_brand, name="list_brand"),
    path("show_brand/<brand_id>", views.show_brand, name="show_brand"),
    path("update_brand/<brand_id>", views.update_brand, name="update_brand"),
    path("add_brand/", views.add_brand, name="add_brand"),

    path("list_model/", views.list_model, name="list_model"),
    path("show_model/<model_id>", views.show_model, name="show_model"),
    path("update_model/<model_id>", views.update_model, name="update_model"),
    path("add_model/", views.add_model, name="add_model"),
    # path("contact/", views.contact, name="contact"), # to jest contact z html form (ladny)
    path("list_driver/", views.list_driver, name="list_driver"),
    path("show_driver/<driver_id>", views.show_driver, name="show_driver"),
    path("update_driver/<driver_id>", views.update_driver, name="update_driver"),
    path("add_driver/", views.add_driver, name="add_driver"),
]
