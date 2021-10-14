from playwright.sync_api import Page

class SearchPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def search_box(self):
        return self.page.wait_for_selector('input[name=q]')

    @property
    def accept_terms(self):
        return self.page.wait_for_selector('button :text("Ich stimme zu")')

    def navigate(self):
        self.page.goto("https://google.com")
        self.page.wait_for_load_state()

    def accept_the_terms(self):
        self.accept_terms.click()
        
    def search(self, textToSearch):
        self.search_box.fill(textToSearch)
        self.search_box.press('Enter')
