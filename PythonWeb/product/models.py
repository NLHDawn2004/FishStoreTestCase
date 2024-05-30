from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images_product/')
    endow = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, related_name='categories', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
