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
   if serializer.is_valid():
      return Response(serializer.errors, status=400)
   
   serializer.save()
  
   return Response({"success": True})

