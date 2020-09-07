from django.contrib import admin
from cars.models import Car, Color


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass
