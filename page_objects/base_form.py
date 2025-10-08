from playwright.sync_api import Page
from config import BASE_URL


class BaseForm:

    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = BASE_URL + url

    def goto(self):
        self.page.goto(self.url)