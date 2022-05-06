from django.urls import path
from .views import *

urlpatterns = [
   path('', index),
   path('search-book', search_book),
   path('borrow-book', borrow_book),
   path('test-post', test_post),
]

