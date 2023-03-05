from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=5)
    symbol = models.CharField(max_length=1)

    class Meta:  
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name