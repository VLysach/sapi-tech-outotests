from pages.base_page import BasePage

class LandingPage(BasePage):

    _nav_items = {
        'About us': "a.menu__link_2K2.w-nav__link",
        'Services': "a.menu__link_2K2.w-nav__link",
        'Careers': "a.menu__link_2K2.w-nav__link",
        'Blog': "a.menu__link_2K2.w-nav__link",
        'Contacts': "a.menu__link_2K2.w-nav__link",
    }

    def open(self) -> None:
        self.open_url("https://sapi-tech.com/en")

    def is_nav_item_visible(self, label: str) -> bool:
        selector = self._nav_items.get(label)
        if not selector:
            raise ValueError(f"Немає пункту '{label}' у навігації")
        return self.find_element(selector).is_visible()

    def get_page_title(self) -> str:
        return self.page.title()

    def is_text_present(self, text: str) -> bool:
        try:
            self.page.wait_for_selector(f"text={text}", timeout=self.timeout)
            return True
        except PlaywrightTimeoutError:
            return False
