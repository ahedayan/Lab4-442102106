from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


tax_rate = 15


def view1(request):
    return HttpResponse("this is a site to calculate tax")


def view2(request, number):
    number = number * (1+(tax_rate/100))
    return HttpResponse(number)


def view3(request):
    return render(request, "My_App/taxRate.html", {"taxRate": tax_rate})
