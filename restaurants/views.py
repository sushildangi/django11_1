from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


# function based view
# def home(request):
#     html_var = 'f Strings'
#     html_ = f'''
#             <!DOCTYPE html>
#             <html lang=en>
#             <head>
#             <title>Hello Ji</title>
#             </head>
#             <body>
#             <h1>Hello World!</h1>
#             <p>This is {html_var} coming through</p>
#             </body>
#             </html>
#
#     '''
#     # return render(request, "home.html", {})
#     return HttpResponse(html_)


def home(request):
    num = random.randint(0, 100000000000)
    return render(request, "base.html", {"html_var": True, "num": num})
