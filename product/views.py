from django.shortcuts import render, HttpResponse
from product.models import Product
# Create your views here.
def product(request):
    allProduct= Product.objects.all()
    context={'allProduct': allProduct}
    return render(request, 'product/product.html', context)
