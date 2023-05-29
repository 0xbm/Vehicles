from django.urls import path
from . import views

app_name = "automobiles"
urlpatterns = [
    path("", views.index, name="index"),
    path("vehicle/", views.vehicle, name="vehicle"),
    # path("contact/", views.contact, name="contact"), # to jest contact z html form (ladny)

]
