from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django import forms
from .forms import ExampleForm
# Django forms validate and sanitize user input, preventing SQL injection
# --- Book Form ---
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


# --- View Books ---
@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/view_books.html', {'books': books})


# --- Create Book ---
@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:view_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/create_book.html', {'form': form})


# --- Edit Book ---
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})


# --- Delete Book ---
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:view_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})



def book_list(request):
    books = Book.objects.all()  # Safe ORM query
    return render(request, "bookshelf/book_list.html", {"books": books})

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, "bookshelf/form_example.html", {"form": form})
