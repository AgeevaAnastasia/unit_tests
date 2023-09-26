import unittest
from unittest.mock import patch
from book_service import BookService, Book


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        with patch('book_service.BookRepository') as mock_book_repository:
            self.book_service = BookService(mock_book_repository)
            mock_book_repository.return_value

    def test_add_book(self):
        self.book = Book(1, 'Руслан и Людмила', 'А.С. Пушкин')
        self.book_service.add_book(self.book)
        self.book_service.book_repository.add_book.assert_called()

    def test_get_books_author(self):
        author = 'А.С. Пушкин'
        self.book_service.get_books_author(author)
        self.book_service.book_repository.get_books_author.assert_called_once_with(author)

    def test_get_all_books(self):
        self.book_service.get_all_books()
        self.book_service.book_repository.return_value()