from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello(request):    
   data = request.data
   print('data=', data)
   return Response({"message" : "Hello world!"})

@api_view(["POST"])
def create_customer(request):
   data = request.data
   print('data=', data)
   # TODO: Validate & Save database
   return Response({"success": True})

