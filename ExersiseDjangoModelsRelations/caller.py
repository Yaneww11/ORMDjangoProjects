import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book


def show_all_authors_with_their_books() -> str:
    author_with_books = []
    authors = Author.objects.all().order_by('id')
    for author in authors:
        books = author.book_set.all()

        if not books:
            continue

        titles = ", ".join(book.title for book in books)
        author_with_books.append(
            f"{author.name} has written - {titles}!"
        )

    return "\n".join(author_with_books)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


# Create authors
author1 = Author.objects.get(name="J.K. Rowling")
author2 = Author.objects.get(name="George Orwell")
author3 = Author.objects.get(name="Harper Lee")
author4 = Author.objects.get(name="Mark Twain")


book4 = Book.objects.get(
    title="1990"
)

# Display authors and their books
authors_with_books = show_all_authors_with_their_books()
print(authors_with_books)

# Delete authors without books
delete_all_authors_without_books()
print(Author.objects.count())
