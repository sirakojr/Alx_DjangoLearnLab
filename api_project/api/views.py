from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    # viewSet that provides full CRUD operations for Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can access
    permission_classes = [permissions.IsAuthenticated]

