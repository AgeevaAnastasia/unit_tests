"""У вас есть класс BookService, который использует интерфейс BookRepository
для получения информации о книгах из базы данных. Ваша задача написать unit-тесты
для BookService, используя Mockito для создания мок-объекта BookRepository."""


class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author


class BookRepository:
    def __init__(self):
        self.repository = []

    def get_books_author(self, author: str):
        books = []
        for book in self.repository:
            if book.author == author:
                books.append(book)
        return books

    def get_all_books(self):
        books = []
        for book in self.repository:
            books.append(book)
        return books

    def add_book(self, book: Book):
        self.repository.append(book)


class BookService:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def add_book(self, book: Book):
        self.book_repository.add_book(book)

    def get_books_author(self, author: str):
        return self.book_repository.get_books_author(author)

    def get_all_books(self):
        return self.book_repository.get_all_books()
