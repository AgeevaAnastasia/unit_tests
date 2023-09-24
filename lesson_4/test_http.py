import unittest
from unittest.mock import Mock

from task_7_http import HttpClient, WebService


class TestWebService(unittest.TestCase):
    def setUp(self) -> None:
        self.webservice = WebService(Mock())

    def test_make_request(self):
        response = self.webservice.make_request('https://google.com', 'weather')
        self.webservice.http_client.get.assert_called()

    def test_no_make_put_request(self):
        response = self.webservice.make_request('https://google.com', 'weather')
        self.webservice.http_client.put.assert_not_called()