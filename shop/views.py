from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.


def index(request):
    products = Products.objects.all()
    print(products)
    n = len(products)
    nSlides = (n+3)//4
    params = {'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We are at contact Us")


def tracker(request):
    return HttpResponse("We are at tracker")


def search(request):
    return HttpResponse("We are at search")


def prod_view(request):
    return HttpResponse("We are at product View")


def checkout(request):
    return HttpResponse("We are at checkout")
