from django.shortcuts import render
from accounts.models import AccountUser
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    account_user = AccountUser.objects.get(user=request.user.id)
    vehicles = Vehicle.objects.filter(account=account_user.account)
    context = {
        "user": request.user,
        "account_user": account_user,
        "vehicles": vehicles
    }
    return render(request, "vehicles/index.html", context)
    