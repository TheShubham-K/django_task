from django.shortcuts import render
import math
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def api(request):
    return render(request, 'calculator.html')


def index(request):
    return render(request, 'index.html')


def result(request):
    n_value = int(request.GET.get('n_value'))
    x_value = int(request.GET.get('x_value'))
    sum = func(n_value, x_value)

    return render(request, 'result.html', {"result": sum})


def func(n, x):
    if(n == 1):
        return 1
    return (1/pow(x,n))+func(n-1, x)
