from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books_view(request):
    books = Book.objects.all()  # Must include this line
    return render(request, "relationship_app/list_books.html", {"books": books})  # Must reference this template
