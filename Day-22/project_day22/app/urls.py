from django.urls import path

from .views import *

urlpatterns = [
    path('create-customer', create_customer),
    path('hello', hello)
]
