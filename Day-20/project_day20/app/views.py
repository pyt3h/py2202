from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'index.html')

#------------------------------------------------------
from django.db.models import Q
from django.shortcuts import HttpResponse
from .models import *
import json
from datetime import datetime, timedelta

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
            'avaiable': book.current_qty > 0
        })
    return HttpResponse(json.dumps(result))

def borrow_book(request):
    body = request.POST
    username = body.get('username')
    barcode = body.get('barcode')

    user = User.objects.filter(username=username).first()
    book_copy = BookCopy.objects.filter(barcode=barcode).first()

    if not user:
        return HttpResponse(json.dumps({'error': 'Người dùng không tồn tại'}))

    if not book_copy:
        return HttpResponse(json.dumps({'error': 'Barcode không hợp lệ'}))

    book_borrow = BoookBorrow()
    book_borrow.user = user
    book_borrow.book_copy = book_copy
    book_borrow.borrow_date = datetime.now()
    book_borrow.deadline = datetime.now() + timedelta(days=book_copy.book.max_duration)
    book_borrow.status = BoookBorrow.Status.BORROWING
    book_borrow.save()

    book_copy.status = BookCopy.Status.BORROWED
    book_copy.save()
    
    book_copy.book.current_qty -= 1
    book_copy.book.save()

    return HttpResponse(json.dumps({'success': True}))

@csrf_exempt
def test_post(request):
    return HttpResponse("Hello")