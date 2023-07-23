from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def contact(request):
    return render(request, 'catalog/contact.html')

def catalog(request):
    return render(request, 'catalog/catalog.html')

def product(request):
    return render(request, 'catalog/product.html')