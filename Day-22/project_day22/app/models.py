from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)

    def __str__(self): return self.fullname

class ProductCategory(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self): return self.name

class Product(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    price = models.IntegerField()

    def __str__(self): return self.name