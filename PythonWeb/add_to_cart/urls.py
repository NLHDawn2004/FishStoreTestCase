from django.urls import path
from . import views
app_name = 'add_to_cart'
urlpatterns = [
    # ... other urls ...
    # path('purchased_products/', views.purchased_products, name='purchased_products'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('ajax/add_to_cart/<int:product_id>/', views.ajax_add_to_cart, name='ajax_add_to_cart'),
    path('delete_from_cart/<int:product_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
]