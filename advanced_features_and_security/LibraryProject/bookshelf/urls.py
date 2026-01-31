from django.urls import path
from bookshelf.views import create_book, edit_book, delete_book, view_books


urlpatterns = [
    path('books/view/', view_books, name='view_books'),
    path('books/create/', create_book, name='create_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
