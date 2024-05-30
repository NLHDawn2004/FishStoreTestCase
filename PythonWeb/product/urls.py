from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # path('add-product/', views.add_product, name='add-product'),

    # path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    # path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('search/', views.search_pro, name='search'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_by_filter/<int:category_id>/', views.product_by_category, name='product_by_category'),
   ]
