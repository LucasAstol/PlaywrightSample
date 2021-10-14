from playwright.sync_api import Page

class ResultsPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def results(self):
        self.page.wait_for_selector('div.hdtb-mitem.hdtb-msel')
        return self.page.query_selector_all('div.yuRUbf')
