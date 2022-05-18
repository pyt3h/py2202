from django.urls import path

from .views import *

urlpatterns = [
    path('search-customer', search_customer),
    path('get-customer-by-phone/<phone>', get_customer_by_phone),
    path('search-product', search_product),
    path('get-product-by-code/<code>', get_product_by_code),
    path('save-cart', save_cart),
    path('hello', hello)
]
