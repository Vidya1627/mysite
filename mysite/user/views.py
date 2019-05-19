from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):
    #products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': []})


def new(request):
    return HttpResponse('New  Products')

