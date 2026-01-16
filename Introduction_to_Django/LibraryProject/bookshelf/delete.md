# Delete and display Output

```python
python manage.py shell
>>>from bookshelf.models import Book
>>> book = Book.objects.get(id=2)
>>> book.delete()
```

### Expected out put

```python
(1, {'bookshelf.Book': 1})
```