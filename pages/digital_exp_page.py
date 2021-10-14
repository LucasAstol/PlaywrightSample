from playwright.sync_api import Page

class DigitalExperience:

    def __init__(self, page: Page):
        self.page = page

    @property
    def title(self):
        return self.page.wait_for_selector('h1')

    @property
    def name(self):
        return self.page.wait_for_selector(':nth-match(.input-group-item > input, 1)')

    @property
    def email(self):
        return self.page.wait_for_selector(':nth-match(.input-group-item > input, 2)')
    
    @property
    def phone(self):
        return self.page.wait_for_selector(':nth-match(.input-group-item > input, 3)')

    @property
    def message(self):
        return self.page.wait_for_selector('.input-group > textarea')

    def consent_check(self):
        return self.page.locator('.accept-conditions input')

    @property
    def captcha(self):
        return self.page.wait_for_selector('id=recaptcha-anchor')

    @property
    def more_info(self):
        return self.page.wait_for_selector('.badge.yellow')

    def complete_form(self, name, email, phone, message):
        self.more_info.click()
        self.name.fill(name)
        self.email.fill(email)
        self.phone.fill('')
        self.phone.fill(phone)
        self.message.fill(message)
        self.consent_check().check()
