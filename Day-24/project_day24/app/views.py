from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello(request):    
   return Response({"message" : "Hello world!"})

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
   customer_list = Customer.objects.filter(phone__icontains=keyword)
   result = CustomerSerializer(customer_list, many=True).data
   return Response(result)

@api_view(['GET'])
def get_customer_by_phone(request, phone):
   customer = Customer.objects.filter(phone=phone).first()
   if not customer:
      return Response({})
   else:
      result = CustomerSerializer(customer).data
      return Response(result)

#==================== Product =================================
class ProductSerializer(ModelSerializer):
   class Meta:
      model = Product
      fields = '__all__'

@api_view(['GET'])
def search_product(request):
   params = request.GET
   keyword = params.get('keyword', '')
   product_list = Product.objects.filter(code__icontains=keyword)
   result = ProductSerializer(product_list, many=True).data
   return Response(result)

@api_view(['GET'])
def get_product_by_code(request, code):
   product = Product.objects.filter(code=code).first()
   if not product:
      return Response({})
   else:
      result = ProductSerializer(product).data
      return Response(result)