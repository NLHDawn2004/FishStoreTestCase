from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login_to, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),

]
