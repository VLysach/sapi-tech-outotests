import pytest
from playwright.sync_api import sync_playwright, Page
from pages.Contacts import ContactsPage

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

FIELD_LABELS = ['Name', 'Your phone number', 'Company', 'Email', 'Message']
CHECKBOX_LABELS = ['Consent', 'Agreement', 'Marketing']

@pytest.mark.parametrize('field_label', FIELD_LABELS)
def test_contacts_fields_are_empty(page, field_label):
    contacts = ContactsPage(page)
    contacts.open()
    assert contacts.is_field_empty(field_label), (
        f"Поле '{field_label}' не порожнє при первинному завантаженні"
    )

@pytest.mark.parametrize('checkbox_label', CHECKBOX_LABELS)
def test_contacts_checkboxes_unchecked(page, checkbox_label):
    contacts = ContactsPage(page)
    contacts.open()
    assert contacts.is_checkbox_unchecked(checkbox_label), (
        f"Чекбокс '{checkbox_label}' встановлений, але очікувався незайнятим"
    )