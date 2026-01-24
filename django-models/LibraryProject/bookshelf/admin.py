from django.contrib import admin

# Register your models here.
from .models import Book

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year') # Add a search bar
    list_filter = ('title', 'author', 'publication_year')  # Add filter options

admin.site.register(Book, MyModelAdmin)