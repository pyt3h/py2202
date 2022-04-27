import json
from django.shortcuts import render, HttpResponse
from .models import *

def search_book(request):
    params = request.GET
    keyword = params.get('keyword', '')
    from_year = params.get('from_year', 1900)
    to_year = params.get('to_year', 2100)
    book_list = Book.objects.filter(
        name__icontains=keyword,
        published_year__lt=to_year,
        published_year__gt=from_year
    )
    print('book_list=', book_list)
    items = []
    for book in book_list:
        items.append({'id': book.id, 'name': book.name})
    result = json.dumps({'books': items})
    return HttpResponse(result)

def index(request):
    return render(request, 'index.html')
