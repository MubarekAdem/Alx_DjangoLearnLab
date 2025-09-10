from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import both Book and Library

# Function-based view: list all books
def list_books_view(request):
    books = Book.objects.all()  # Must be explicitly included
    return render(request, "relationship_app/list_books.html", {"books": books})  # Must reference template

# Class-based view: display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Must reference template
    context_object_name = "library"  # Must be 'library' for template access
