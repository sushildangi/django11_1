from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    num = random.randint(0, 100000000000)
    some_list = [num, random.randint(0, 100000000000), random.randint(0, 100000000000), random.randint(0, 100000000000)]
    context = {
        "bool_item": True,
        "num": num,
        "some_list": some_list,
    }
    return render(request, "base.html", context)
