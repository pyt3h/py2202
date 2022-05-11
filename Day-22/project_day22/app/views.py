from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET', 'POST'])
def hello(request):    
   data = request.data
   print('data=', data)
   return Response({"message" : "Hello world!"})

@api_view(["POST"])
def create_customer(request):
   data = request.data
   print('data=', data)
   
   serializer = CustomerSerializer(data=data)
   
   if not serializer.is_valid():
      return Response(serializer.errors, status=400)
   
   serializer.save()
  
   return Response({"success": True})

@api_view(['GET'])
def search_customer(request):
   params = request.GET # {'keyword':'Nguyen Van A'}
   keyword = params.get('keyword', '')
   customer_list = Customer.objects.filter(
      fullname__icontains=keyword
   )
   #result = []
   #for customer in customer_list:
   #   result.append({
   #      'id': customer.id,
   #      'fullname':customer.fullname,
   #      'phone': customer.phone
   #   })
   result = CustomerSerializer(customer_list,many=True).data
   return Response(result)