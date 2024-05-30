from django.contrib import admin
from product.models import Product, Category


class CategoryInline(admin.TabularInline):
    model = Category.products.through
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]
    exclude = ('categories',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
