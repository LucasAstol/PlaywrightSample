from pages.digital_exp_page import DigitalExperience
from pages.home_page import HomePage
from playwright.sync_api import Page
from pages.success_stories import SucessStories

from pages.what_do_page import WhatWeDo

def test_access_digital_experience(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.accept_all_cookies.click()
    home_page.english_selector.click()
    home_page.what_we_do.click()

    what_do_page = WhatWeDo(page)
    assert what_do_page.title.is_visible()
    
    what_do_page.digital_experience.click()

    digital = DigitalExperience(page)
    digital.page.wait_for_load_state()
    assert digital.title.is_visible()
    digital.complete_form('Vincenzo', 'vincenzo@gmail.com', '123456', 'Io sonno Vincenzo!')


def test_sucess_stories(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.accept_all_cookies.click()
    home_page.english_selector.click()
    home_page.success_stories.click()

    success_stories = SucessStories(page)
    assert "SUCCESS STORIES" == success_stories.title.inner_text()
    
    success_stories.keep_reading.click()
    success_stories.aapp_category.click()
    success_stories.keep_reading.click()

    assert success_stories.client_card.count() == 5
    assert success_stories.card_visible('SERIDA')

