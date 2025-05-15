import pytest
from playwright.sync_api import sync_playwright, Page
from pages.SapiTechMain import LandingPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser) -> Page:
    page = browser.new_page()
    yield page
    page.close()

NAV_LABELS = ['About us', 'Services', 'Careers', 'Blog', 'Contacts']


def test_navigation_items(page):
    landing = LandingPage(page)
    landing.open()

    # Перевірка URL
    assert page.url.startswith("https://sapi-tech.com/en"), f"Очікували URL починатися на https://sapi-tech.com/en, але отримали {page.url}"

    # Перевірка пунктів навігації
    for label in NAV_LABELS:
        assert landing.is_nav_item_visible(label), f"Пункт навігації '{label}' не відображається"


def test_title_and_blog_text(page):
    landing = LandingPage(page)
    landing.open()
    title = landing.get_page_title()
    assert "Sapiens Tech | Implementation of SAP and other IT solutions" in title, f"Очікували що тайтл містить 'Sapi Tech', але отримали '{title}'"


def test_blog_text(page):
    landing = LandingPage(page)
    landing.open()
    assert landing.is_text_present("Sapiens Tech Blog"), "Текст 'Sapiens Tech Blog' не знайдено на сторінці"
