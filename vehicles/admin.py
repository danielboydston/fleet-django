from django.contrib import admin

from .models import Category, Make, Model, Vehicle, Meter, MeterReading
# Register your models here.
admin.site.register(Category)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Vehicle)
admin.site.register(Meter)
admin.site.register(MeterReading)