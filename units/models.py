from django.db import models

# Create your models here.
class UnitCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:  
        verbose_name_plural = 'Unit categories'

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=5) 
    category = models.ForeignKey(UnitCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UnitConversion(models.Model):
    unit_from = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit_from")
    unit_to = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit_to")
    formula = models.TextField()

    def __str__(self):
        return f"{self.unit_from.name} to {self.unit_to.name}"
