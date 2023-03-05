from django.contrib import admin

from .models import Unit, UnitCategory, UnitConversion

# Register your models here.
admin.site.register(Unit)
admin.site.register(UnitCategory)
admin.site.register(UnitConversion)