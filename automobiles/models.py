from django.db import models


# Create your models here.

class Vehicle(models.Model):
    brand = models.CharField('Brand', max_length=10)
    model = models.CharField('Model', max_length=10)
    reg_number = models.CharField('Registration Number', max_length=10)

    # def __str__(self):
    #     return self.brand
