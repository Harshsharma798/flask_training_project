from seleniumbase import BaseCase

class PageTest(BaseCase):
    def test_page_meta(self):
        self.open("https://www.google.com/")
        self.assert_title("Google")

