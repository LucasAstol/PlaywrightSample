from playwright.sync_api import Page

class HomePage:
    
    def __init__(self, page: Page):
        self.page = page

    @property
    def accept_all_cookies(self):
        return self.page.wait_for_selector('id=gdpr-cookie-accept-all')

    @property
    def english_selector(self):
        return self.page.wait_for_selector('div.languages span[lang="en-US"]')

    @property
    def what_we_do(self):
        return self.page.wait_for_selector('.menu-principal a.has-children:has-text("What we do")')

    @property
    def success_stories(self):
        return self.page.wait_for_selector('.badge-secondary:has-text("Success stories")')

    def navigate(self):
        self.page.goto("https://www.izertis.com")
        self.page.wait_for_load_state()
