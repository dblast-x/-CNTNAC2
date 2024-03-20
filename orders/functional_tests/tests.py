from time import sleep
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_visit_home_page(self):
        browser = self.browser
        browser.get(self.live_server_url)

        self.assertIn("Count & Account", browser.title)
        header_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Orders", header_text)
