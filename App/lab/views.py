from django.shortcuts import render
from lab.models import Car, Address, Sales, User
from django.views.generic import View

# Create your views here.
# def base(request):
#     return render(request, 'lab/base.html', {})

def main(request):
    return render(request, 'lab/main.html', {})


class CarView(View):
    def get(self, request):
        model_row = Car.objects.all()
        return render(request, 'lab/model_row.html', {'model_row': model_row})


class AddressView(View):
    def get(self, request):
        address = Address.objects.all()
        return render(request, 'lab/address.html', {'address': address})


class SalesView(View):
    def get(self, request):
        sales = Sales.objects.all()
        return render(request, 'lab/sales.html', {'sales': sales})


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'lab/users.html', {'users': users})

