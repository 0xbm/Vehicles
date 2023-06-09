from django.contrib import admin
from .models import Brand, Model, Vehicle, Driver

# Register your models here.
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Driver)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('brand', 'model', 'driver')
