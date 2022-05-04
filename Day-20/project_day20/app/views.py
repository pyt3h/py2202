from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

#------------------------------------------------------
from django.db.models import Q
from django.shortcuts import HttpResponse
from .models import *
import json

def search_book(request):
    params = request.GET
    keyword = params.get('keyword', '')
    category_id = params.get('category_id')
    start_year = params.get('start_year')
    end_year = params.get('end_year')
    books = Book.objects.all()
    
    if keyword != '':
        books = books.filter(
            Q(name__icontains=keyword) |
            Q(isbn__icontains=keyword)
        )

    if category_id:
        books = books.filter(category__id=category_id)

    if start_year:
        books = books.filter(...)

    if end_year:
        books = books.filter(...)

    result = []
    for book in books:
        result.append({
            'id': book.id,
            'name': book.name,
            'isbn': book.isbn,
            'author': book.author.name,
        })
    return HttpResponse(json.dumps(result))