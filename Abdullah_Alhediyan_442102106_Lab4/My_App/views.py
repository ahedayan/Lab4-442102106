from django.shortcuts import render
# Create your views here.


tax_rate = 15


def view1(request):
    return render(request, "My_App/defaultPath.html")


def view2(request, number):
    number = number * (1+(tax_rate/100))
    return render(request, "My_App/calculate.html", {"number": number})


def view3(request):
    return render(request, "My_App/taxRate.html", {"taxRate": tax_rate})
