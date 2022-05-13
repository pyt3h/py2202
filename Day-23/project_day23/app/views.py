from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello(request):    
   return Response({"message" : "Hello world 123!"})

from rest_framework.serializers import ModelSerializer
from .models import *

class CustomerSerializer(ModelSerializer):
   class Meta:
      model = Customer
      fields = '__all__'

@api_view(['GET'])
def search_customer(request):
   params = request.GET
   keyword = params.get('keyword', '')
   customer_list = Customer.objects.filter(fullname__icontains=keyword)
   result = CustomerSerializer(customer_list, many=True).data
   return Response(result)

@api_view(['POST'])
def create_customer(request):
   serializer = CustomerSerializer(data=request.data)
   if not serializer.is_valid():
      return Response(serializer.errors,status=404)
   serializer.save()
   return HttpResponse({'success':True})