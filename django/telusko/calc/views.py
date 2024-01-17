from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Ram Gopal'})

def add(request):

    val1 = int(request.GET["Num 1"])
    val2 = int(request.GET["Num 2"])
    res = val1 + val2

    return render(request, 'result.html', {'result':res})