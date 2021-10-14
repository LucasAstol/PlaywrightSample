from playwright.sync_api import Page

class SucessStories:

    def __init__(self, page: Page):
        self.page = page

    @property
    def title(self):
        return self.page.wait_for_selector('p.title')

    @property
    def keep_reading(self):
        return self.page.locator('a.link-read-more')

    @property
    def aapp_category(self):
        return self.page.wait_for_selector('a.badge-section:has-text("AA.PP")')

    @property
    def client_card(self):
        return self.page.locator('div.row.content-img')

    @property
    def client_card_text(self):
        return self.client_card.wait_for_selector('div.title')

    def card_visible(self, card_title):
        return self.page.wait_for_selector('div.title:has-text("'+ card_title +'")').is_visible()
