from pages.results_page import ResultsPage
from pages.search_page import SearchPage

from playwright.sync_api import Page

def test_search(page: Page):
    search_page = SearchPage(page)

    search_page.navigate()
    search_page.accept_the_terms()
    search_page.search('globetesting')


    results_page = ResultsPage(page)
    assert len(results_page.results) == 10
