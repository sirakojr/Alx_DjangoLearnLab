from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year can't be future.")
        return value

class NestedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "publication_year"]

class AuthorSerializer(serializers.ModelSerializer):
    books = NestedBookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["name", "books"]


# >>> authorGeo = Author.objects.get(id=2)
# >>> book = Book.objects.create(title="1984", publication_year=1949, author=authorGeo)
# >>> book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=authorGeo)
# >>> serializer = AuthorSerializer(authorGeo)
# >>> serializer.data