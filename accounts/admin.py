from django.contrib import admin

# Register your models here.
#from django.contrib.auth.admin import UserAdmin
from .models import AccountUser, Account

admin.site.register(AccountUser)
admin.site.register(Account)