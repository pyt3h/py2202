from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    published_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

# --------------------------- Shop -----------------------------------
class ProductCategory(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, null=True, blank=True)