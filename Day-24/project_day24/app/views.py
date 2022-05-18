from datetime import datetime
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

#====================== Cart ==============================
@api_view(['POST'])
def save_cart(request):
   data = request.data
   customer_id = data.get("customer_id")
   
   if customer_id and not Customer.objects.filter(pk=customer_id).exists():
      return Response({'error': 'Khách hàng không tồn tại'}, 
                     status=404)

   items = data.get("items", [])
   for item in items:
      qty = item.get("qty", 0)
      product_id = item.get("product_id")
      if not product_id:
         return Response({'error': 'Thiếu sản phẩm trong danh mục hàng'}, 
                           status=500)

      if not Product.objects.filter(pk=product_id).exists():
         return Response({'error': f'Sản phẩm không tồn tại: {product_id}'}, 
                           status=404)

      if int(qty) <= 0:
         return Response({'error': f'Số lượng không hợp lệ: {qty}'}, 
                        status=500)
   
   cart = Cart.objects.create(
      customer=Customer(pk=customer_id),
      date=datetime.now(),
      total=0
   )
   for item in items:
      qty = int(item["qty"])
      product_id = item["product_id"]
      product = Product.objects.get(pk=product_id)
      cart_item = CartItem.objects.create(
         cart=cart,
         product=product,
         price_unit=product.price,
         qty=qty,
         sub_total=qty*product.price
      )
      cart.total += cart_item.sub_total
   
   cart.save()       # save total

   return Response({'success': True})