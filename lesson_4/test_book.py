import unittest
from unittest.mock import patch

from task_4_book import BookingService


class TestBook(unittest.TestCase):
    @patch('task_4_book.HotelService')
    def test_book(self, mock_book):
        self.booking_service = BookingService(mock_book)
        room_id = 6
        self.booking_service.book_room(room_id)
        self.booking_service.hotel_service.is_room_available.assert_called_once_with(room_id)
