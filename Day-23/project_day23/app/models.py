from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image = models.ImageField(blank=True,null=True, upload_to='static/images')

    def __str__(self): return self.fullname