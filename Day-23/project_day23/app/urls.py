from django.urls import path

from .views import *

urlpatterns = [
    path('search-customer', search_customer),
    path('create-customer', create_customer),
    path('hello', hello)
]
