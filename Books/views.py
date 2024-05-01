from django.shortcuts import render
from .models import Book

def landing_page(request):
    return render(request, 'landing_page.html')

def browse_books(request):
    books = Book.objects.all()
    return render(request, 'browse_books.html', {'books': books})
