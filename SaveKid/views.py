from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'base.html')

def buy_page(request):
    return render(request, 'buy_product.html')

def about_page(request):
    return render(request, 'about.html')
