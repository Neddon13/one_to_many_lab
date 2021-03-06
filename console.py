import pdb
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository 


author_1 = Author("J.K.Rowling")
author_repository.save(author_1)
author_2 = Author("Stephen King")
author_repository.save(author_2) 


book_1 = Book("The Stand", "Horror", author_2)
book_repository.save(book_1)
book_2 = Book("The Shining", "Horror", author_2)
book_repository.save(book_2)
book_3 = Book("Harry Potter", "Fantasy", author_1)
book_repository.save(book_3)
book_4 = Book("Fantastic Beasts", "Fantasy", author_1)
book_repository.save(book_4)

for book in book_repository.select_all():
    print(book.__dict__)

book_repository.delete(1)