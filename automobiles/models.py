from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField('Brand', max_length=10)

    def __str__(self):
        return self.name.title()


class Model(models.Model):
    name = models.CharField('Model', max_length=10)

    def __str__(self):
        return self.name.title()


class Driver(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)

    def __str__(self):
        return self.first_name.title() + ' ' + self.last_name.title()


class Vehicle(models.Model):
    name = models.CharField('Name', max_length=20)  # blank=False,
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)  # null=True
    model = models.ForeignKey(Model, blank=True, null=True, on_delete=models.CASCADE)  # null=True
    reg_num = models.CharField('Registration Number', max_length=10, blank=True)
    tech_inspection = models.DateField("Technical Inspection", blank=True, null=True)
    vin_num = models.CharField('VIN Number', max_length=17, blank=True)
    driver = models.ManyToManyField(Driver, blank=True)
    description = models.TextField(blank=True)
    vehicle_image = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        return self.name.title()