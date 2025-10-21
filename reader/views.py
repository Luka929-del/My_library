from django.shortcuts import render
from book.models import Book
from .models import Reader

def reader_form(request):
    books = Book.objects.all()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        favorite_book_id = request.POST.get('favorite_book')
        favorite_book = Book.objects.get(id=favorite_book_id) if favorite_book_id else None

        reader = Reader(first_name=first_name, last_name=last_name, age=age, favorite_book=favorite_book)
        return render(request, 'reader/reader_detail.html', {'reader': reader})
    return render(request, 'reader/reader_form.html', {'books': books})
