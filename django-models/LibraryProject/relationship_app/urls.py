from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from .views import (
    list_books_view,
    LibraryDetailView,
    register_view,

)


urlpatterns = [
     path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    
    # Function-based registration view
    path("register/", views.register_view, name="register"),
    
    # Other existing views
    path("books/", views.list_books_view, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
