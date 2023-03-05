from django.contrib.auth.models import User
from django.db import models
from currency.models import Currency

class Account(models.Model):
    ACCOUNT_STATUS = (
        ('active','Active'),
        ('suspended','Suspended'),
        ('inactive','Inactive')
    )
    company = models.CharField(max_length=50,blank=True,default="")
    status = models.CharField(max_length=30,choices=ACCOUNT_STATUS,default='active')
    currency = models.ForeignKey(Currency, on_delete=models.RESTRICT, default=1)

    def __str__(self):
        if len(self.company) == 0:
            output = self.id
        else:
            output = f"{self.company}"
        return output

class AccountUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} - {self.user}"