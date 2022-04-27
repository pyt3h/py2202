from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Book(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    published_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self): return self.name

# --------------------------- Shop -----------------------------------
class ProductCategory(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, null=True, blank=True)

class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image_url = models.CharField(max_length=1024)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

class SaleOrder(models.Model):
    qty = models.IntegerField()
    price_unit = models.IntegerField()
    total = models.IntegerField()
    order_date = models.DateTimeField()
    status = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
