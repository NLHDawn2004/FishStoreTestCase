from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from add_to_cart.models import Cart
from product.models import Product
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    products = Product.objects.all()
    products_endow = Product.objects.filter(endow=True)
    return render(request, 'home/index.html', {"products": products, "products_endow": products_endow})


def add_to_cart(request, product_id):
    # product = get_object_or_404(Product, pk=product_id)
    # cart, cart_created = Cart.objects.get_or_create(user=request.user)
    # cart_item, created = cart.cartitem_set.get_or_create(product=product, defaults={'quantity': 1})
    # if not created:
    #     cart_item.quantity += 1
    #     cart_item.save()
    # else:
    #     cart_item.quantity = 1
    #     cart_item.save()
    return redirect('home:base')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:login')
    return render(request, 'home/register.html', {'form': form})


def login_to(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect('home:base')

    return render(request, 'home/login.html')


def log_out(request):
    try:
        logout(request)
        return redirect('home:base')
    except Exception as e:
        return HttpResponse("ERROR")


def cart(request):
    return render(request, 'home/cart.html')
