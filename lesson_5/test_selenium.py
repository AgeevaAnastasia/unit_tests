import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(executable_path='chromedriver.exe'))

    def test_selenium(self):
        self.driver.get('https://www.google.ru/')
        elem = self.driver.find_element(By.NAME, 'q')
        elem.send_keys('Selenium')
        elem.send_keys(Keys.RETURN)
        self.assertIn('https://www.selenium.dev', self.driver.find_element(By.XPATH, '/html/body').text)
        # self.assertIn('https://www.selenium.dev', self.driver.page_source)

    def tearDown(self) -> None:
        self.driver.close()
