import unittest
from unittest.mock import Mock


class TestIterator(unittest.TestCase):
    def setUp(self) -> None:
        self.iterator = Mock()
        self.iterator.next = iter(['Hello', 'world']).__next__

    def test_iterator(self):
        result = self.iterator.next() + " " + self.iterator.next()
        self.assertEqual(result, 'Hello world')
