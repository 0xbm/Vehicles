from django.urls import path
from . import views

app_name = 'pricing'
urlpatterns = [
    path("", views.pricing, name="pricing"),
    path("pay_3", views.pay_3, name="pay_3"),
    path("pay_6", views.pay_6, name="pay_6"),
    path("pay_9", views.pay_9, name="pay_9"),
    path("pay_12", views.pay_12, name="pay_12"),
]
