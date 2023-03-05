from django.db import models
from accounts.models import Account
from units.models import UnitCategory, Unit
from currency.models import Currency

# Create your models here.
   
class Category(models.Model):
    name = models.CharField(max_length=30)
    meter_unit_category = models.ForeignKey(UnitCategory, on_delete=models.RESTRICT)

    class Meta:  
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Make(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.make} {self.name}"

class Vehicle(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    trim = models.CharField(max_length=50, blank=True)
    meter_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="meter_unit")
    fuel_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="fuel_unit")
    meter_correction_ratio = models.DecimalField(max_digits=4, decimal_places=3, default=1.0)
    currency = models.ForeignKey(Currency, on_delete=models.RESTRICT, default=1)
    
    def __str__(self):
        return f"{self.year} {self.model.make.name} {self.model.name} {self.trim}"

class Meter(models.Model):
    name = models.CharField(max_length=30)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    install_date = models.DateField()
    install_vehicle_reading = models.PositiveIntegerField()
    install_meter_reading = models.PositiveIntegerField()
    remove_date = models.DateField(null=True, blank=True)

    def __str__(self):
        name_str = ""
        if len(self.name) > 0:
            name_str = f" {self.name} "
        return f"{self.vehicle}{name_str}"

class MeterReading(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    reading_date = models.DateField()
    reading = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.reading}"
 