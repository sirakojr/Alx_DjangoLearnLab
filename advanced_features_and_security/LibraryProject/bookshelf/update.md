# Update and display Output

```python
>>> book = Book.objects.get(id=2)
>>> book.title = "Nineteen Eighty-Four"
>>> print(book)
```

### Expected out put

```python
Nineteen Eighty-Four | George Orwell | 1949
```