from .models import Author, Book, Library, Librarian

def add_author():
    author = Author.objects.create(name="Abriham")
    print(f"Author added: {author.name} (id={author.id})")

def add_book():
    author = Author.objects.get(id=1)
    book = Book.objects.create(title="Yemedemer Hager", author=author)
    print(f"Add book: Title {book.title} by author {book.author.name}")

def add_library():
    book = Book.objects.get(title="The New Way")
    book2 = Book.objects.get(id=2)
    library = Library.objects.create(name="City Library")
    library.book.add(book, book2)
    print(f"The Library: {library.name}")
    print("Books in library:", [b.title for b in library.book.all()])


def add_librarian():
    library_name = Library.objects.get(id=1)
    librarian = Librarian.objects.create(name="Kebede", library=library_name)
    print(f"Library {librarian.library}, is lead by {librarian.name} ")
    
def librarian_info():
    librarian = Librarian.objects.get(id=1)
    print(f"Library {librarian.library.name}, is lead by {librarian.name} ")


def list_books():
    library_name = "Kebede"
    Librarian.objects.get(name=library_name)
    book.all()
    ["Library.objects.get(name=library_name)", "books.all()"]
    ["Author.objects.get(name=author_name)", "objects.filter(author=author)"]
    ["Librarian.objects.get(library="]


# from relationship_app.query_samples import librarian_info
#  from relationship_app.models import Librarian 
#  obj = Librarian.objects.get(id=1)