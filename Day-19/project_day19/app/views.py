import json
from django.shortcuts import render, HttpResponse
from .models import *

def search_book(request):
    params = request.GET
    keyword = params.get('keyword', '')
    book_list = Book.objects.filter(name__icontains=keyword)
    print('book_list=', book_list)
    items = []
    for book in book_list:
        items.append({'id': book.id, 'name': book.name})
    result = json.dumps({'books': items})
    return HttpResponse(result)

def index(request):
    return render(request, 'index.html')
