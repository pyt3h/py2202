import json
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def save_data(request):
    data = request.POST
    print('data=', data)
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    c = a + b
    return HttpResponse(f'Tổng 2 số : {c}')

def index(request):
    return render(request, 'index.html')

def hello(request):
    data = request.GET
    username = data.get('username', '')
    return HttpResponse(f"<b>Hello {username}</b>")

def add_2_number(request):
    data = request.GET
    print('data=', data)
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    c = a + b
    return HttpResponse(f'Tổng 2 số : {c}')

data = {
  'Hanoi': {'temp': 19, 'humidity': 90},
  'HCMCity': {'temp': 32, 'humidity': 80},
}

def get_weather_data(request):
    location = request.GET.get('location')
    result = data.get(location, {'error': 'Unknown location'})
    
    return HttpResponse(json.dumps(result), 
            content_type='application/json')