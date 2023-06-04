from django.db import models


# Create your models here.


class Brand(models.Model):
    brand = models.CharField('Brand', max_length=10)

    # def brand_capitalize(self):
    #     return f"{self.brand_capitalize}".title()

    def __str__(self):
        # self.name = self.name.title()
        return self.brand


class Model(models.Model):
    model = models.CharField('Model', max_length=10)

    # def model_capitalize(self):
    #     return f"{self.model_capitalize}".title()

    def __str__(self):
        # self.name = self.name.title()
        return self.model


class Vehicle(models.Model):
    name = models.CharField('Name', max_length=20)
    brand = models.ManyToManyField(Brand, blank=True)
    model = models.ManyToManyField(Model, blank=True)
    # brand = models.CharField(max_length=10)
    # model = models.CharField(max_length=10)
    reg_number = models.CharField('Registration Number', max_length=10)
    tech_insp = models.DateField("Technical Inspection")
    # driver = models.CharField('Driver', max_length=20)
    # description = models.TextField(blank=True)

    def full_name(self):
        return f"{self.brand} {self.model}".title()

    def __str__(self):
        # self.name = self.name.title()
        return self.full_name()
