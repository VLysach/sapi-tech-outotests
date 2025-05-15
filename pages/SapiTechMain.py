from pages.base_page import BasePage

class LandingPage(BasePage):
    """Page Object для лендингу Sapi Tech"""

    # селектори
    _nav_items = {
        'About us': "a.menu__link_2K2.w-nav__link",
        'Services': "a.menu__link_2K2.w-nav__link",
        'Careers': "a.menu__link_2K2.w-nav__link",
        'Blog': "a.menu__link_2K2.w-nav__link",
        'Contacts': "a.menu__link_2K2.w-nav__link",
    }
    _footer = "css=footer"

    def open(self) -> None:
        """Відкрити лендинг."""
        self.open_url("https://sapi-tech.com/en")

    def is_nav_item_visible(self, label: str) -> bool:
        """Перевірити, що пункт навігації з текстом label видно."""
        selector = self._nav_items.get(label)
        if not selector:
            raise ValueError(f"Нет пункту навігації з назвою {label}")
        return self.find_element(selector).is_visible()

    def get_page_title(self) -> str:
        """Повернути заголовок сторінки."""
        return self.page.title()

    def is_text_present(self, text: str) -> bool:
        """Перевірити, що на сторінці присутній заданий текст."""
        # шукаємо будь-де на сторінці
        try:
            self.page.wait_for_selector(f"text={text}", timeout=self.timeout)
            return True
        except PlaywrightTimeoutError:
            return False