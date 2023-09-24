import unittest
from unittest.mock import Mock

from task_6_database import Database, DataProcessor


class TestDataProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.data_processor = DataProcessor(Mock())

    def test_data_processor(self):
        result = self.data_processor.db_query('select * from abstract_table')
        self.data_processor.database.query.assert_called_once()
