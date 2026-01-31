# Create Operation in Django Shell

```python
python manage.py shell
>>>from bookshelf.models import book
>>> object1 = Book.objects.create(title="1984", author="George Orwell", publication_year="1949")
```
