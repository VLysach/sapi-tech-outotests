import pytest
from pages.SapiTechMain import LandingPage

NAV_LABELS = ['About us', 'Services', 'Careers', 'Blog', 'Contacts']

@pytest.mark.parametrize('label', NAV_LABELS)
def test_nav_items_visible(page, label):
    landing = LandingPage(page)
    landing.open()

    assert page.url.startswith("https://sapi-tech.com/en"), f"Невірний URL: {page.url}"

    assert landing.is_nav_item_visible(label), f"'{label}' не видно"

def test_title_visible(page):
    landing = LandingPage(page)
    landing.open()
    assert "Sapiens Tech | Implementation of SAP and other IT solutions" in landing.get_page_title(), "Заголовок сторінки не містить 'Sapi Tech'"

def test_blog_text_visible(page):
    landing = LandingPage(page)
    landing.open()
    assert landing.is_text_present("Sapiens Tech Blog"), "Текст 'Sapiens Tech Blog' відсутній"