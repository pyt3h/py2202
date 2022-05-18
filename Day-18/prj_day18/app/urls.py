from django.urls import path
from .views import *

urlpatterns = [
   path('', index),
   path('hello', hello),
   path('add-2-number', add_2_number),
   path('get-weather-data', get_weather_data),
   path('save-data', save_data),
]

