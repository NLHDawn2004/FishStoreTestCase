from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import *


# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:base')
        else:
            return redirect('product:add_product')
    else:
        form = ProductForm()
        return render(request, 'product/add_product.html', {'form': form})


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('home:base')


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home:base')
        else:
            return redirect('product:update_product', product_id=product_id)
    else:
        form = ProductForm(instance=product)
        return render(request, 'product/update_product.html', {'form': form})


def search_pro(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        products = Product.objects.filter(name__icontains=search)
        # Filter the products by name insensitive case

        return render(request, 'home/search_product.html', {'products': products})
    else:
        return redirect('home:base')


def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'product/product_list.html', {'products': products})


def product_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.products.all()
    return render(request, 'product/product_list.html', {'products': products})
