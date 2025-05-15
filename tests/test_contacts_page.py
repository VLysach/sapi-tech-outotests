import pytest
from pages.Contacts import ContactsPage


FIELD_LABELS = ['Name', 'Your phone number', 'Company', 'Email', 'Message']
CHECKBOX_LABELS = ['Consent', 'Agreement', 'Marketing']

@pytest.mark.parametrize('field_label', FIELD_LABELS)
def test_contacts_fields_are_empty(page, field_label):
    contacts = ContactsPage(page)
    contacts.open()
    assert contacts.is_field_empty(field_label), f"Поле '{field_label}' має значення"

@pytest.mark.parametrize('checkbox_label', CHECKBOX_LABELS)
def test_contacts_checkboxes_unchecked(page, checkbox_label):
    contacts = ContactsPage(page)
    contacts.open()
    assert contacts.is_checkbox_unchecked(checkbox_label), f"Чекбокс '{checkbox_label}' встановлений"