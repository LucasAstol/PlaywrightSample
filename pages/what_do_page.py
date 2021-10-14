from playwright.sync_api import Page

class WhatWeDo:

    def __init__(self, page: Page):
        self.page = page

    @property
    def title(self):
        return self.page.wait_for_selector('div.menu-services > h2')

    @property
    def what_list(self):
        return self.page.query_selector_all('ul.list-unstyled a')

    @property
    def digital_experience(self):
        return self.page.wait_for_selector("a:has(span:has-text('DIGITAL EXPERIENCE'))")
