from django.db import models


# Create your models here.

class Vehicle(models.Model):
    # id =
    name = models.CharField('Name', max_length=20, default=None, blank=True)
    brand = models.CharField('Brand', max_length=10)
    model = models.CharField('Model', max_length=10)
    reg_number = models.CharField('Registration Number', max_length=10)
    tech_insp = models.DateTimeField("Technical Inspection")

    def full(self):
        return f"{self.brand} {self.model}".title()

    def __str__(self):
        # self.name = self.name.title()
        return self.full()

# class Brand(models.Model):
#     brand = models.CharField('Brand', max_length=10)
