from django.http import JsonResponse
from django.shortcuts import render

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from product.models import Product
from django.shortcuts import get_object_or_404


# def add_to_cart(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     cart, cart_created = Cart.objects.get_or_create(user=request.user)
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     else:
#         cart_item.quantity = 1
#         cart_item.save()
#
#     return redirect('home:base')


def ajax_add_to_cart(request, product_id):
    print('ajax_add_to_cart')
    product = Product.objects.get(pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    # cart_items, created = cart.cartitem_set.get_or_create(product=product, defaults={'quantity': 1})
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()

    return JsonResponse({'success': True})


def delete_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=request.user)

    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()

    return redirect('add_to_cart:view_cart')


def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    # total price products in cart
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity

    return render(request, 'add_to_cart/purchased_products.html',
                  {'cart_items': cart_items, 'total_price': total_price})
