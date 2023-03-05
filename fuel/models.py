from django.db import models
from units.models import Unit
from vehicles.models import MeterReading
from currency.models import Currency

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Fill(models.Model):
    meter_reading = models.ForeignKey(MeterReading, on_delete=models.CASCADE)
    fuel_grade = models.ForeignKey(Grade, on_delete=models.RESTRICT)
    qty = models.DecimalField(max_digits=8, decimal_places=3)
    local_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    station = models.CharField(max_length=50)
    full = models.BooleanField(default=True)
    local_price_per_unit = models.DecimalField(max_digits=7, decimal_places=3)
    local_currency = models.ForeignKey(Currency, on_delete=models.RESTRICT)
    account_price_per_unit = models.DecimalField(max_digits=7, decimal_places=3)
    
    def __str__(self):
        return f"{self.meter_reading} {self.qty} {self.local_unit}"