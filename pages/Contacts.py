from pages.base_page import BasePage

class ContactsPage(BasePage):
    _fields = {
        'Name':                    '//*[@id="67436a98430a513bbcc95f05-e11f5daa-c3e3-43cc-a0e2-9a7083f4504e"]',
        'Your phone number':       '//*[@id="67436a98430a513bbcc95f05-contactForm_phoneNumber"]',
        'Company':                 '//*[@id="67436a98430a513bbcc95f05-97d7dd74-b038-44b8-a7fd-88cf7eff161e"]',
        'Email':                   '//*[@id="67436a98430a513bbcc95f05-contactForm_email"]',
        'Message':                 '//*[@id="67436a98430a513bbcc95f05-962ba6b0-f5e7-4fe4-be44-3bff517e600a"]',
    }
    _checkboxes = {
        'Consent':           "label:has-text('I provide my consent to the processing of my personal data') >> input[type='checkbox']",
        'Agreement':         "label:has-text('I have read and agree to the Privacy Policy') >> input[type='checkbox']",
        'Marketing':         "label:has-text('I agree that SAPIENS TECH may send me marketing materials') >> input[type='checkbox']",
    }

    def open(self) -> None:
        self.open_url("https://sapi-tech.com/en/contacts")

    def is_field_empty(self, field_label: str) -> bool:
        selector = self._fields.get(field_label)
        if not selector:
            raise ValueError(f"Немає поля '{field_label}'")
        el = self.find_element(selector)
        return el.input_value() == ''

    def is_checkbox_unchecked(self, label: str) -> bool:
        selector = self._checkboxes.get(label)
        if not selector:
            raise ValueError(f"Немає чекбоксу '{label}'")
        self.find_element(selector)
        return not self.is_checked(selector)
