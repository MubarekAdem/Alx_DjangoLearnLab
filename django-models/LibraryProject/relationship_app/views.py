from django.views.generic import DetailView
from .models import Library  # Must include this import

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Must reference this template
    context_object_name = "library"  # Must use this context variable
