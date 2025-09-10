from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books_view, name="list_books"),
    path("register/", views.register_view, name="register"),
 path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
