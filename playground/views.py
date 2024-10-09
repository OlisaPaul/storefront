from django.shortcuts import render
from django.http import HttpResponse


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    """Test view function"""
    x = calculate()
    return render(request, "hello.html", {"name": "Paul Olisaeloka"})
