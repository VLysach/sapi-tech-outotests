from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class BasePage:
    def __init__(self, page: Page, timeout: int = 10_000):
        self.page = page
        self.timeout = timeout

    def open_url(self, url: str) -> None:
        self.page.goto(url)

    def find_element(self, selector: str):
        try:
            return self.page.wait_for_selector(selector, state="visible", timeout=self.timeout)
        except PlaywrightTimeoutError:
            raise AssertionError(f"Елемент за селектором {selector} не відобразився за {self.timeout}ms")

    def click_element(self, selector: str) -> None:
        el = self.find_element(selector)
        el.click()

    def enter_text(self, selector: str, text: str, clear_first: bool = True) -> None:
        el = self.find_element(selector)
        if clear_first:
            el.fill(text)
        else:
            el.type(text)

    def get_text(self, selector: str) -> str:
        el = self.find_element(selector)
        return el.text_content() or ""
    
    def is_checked(self, selector: str) -> bool:
        return self.page.locator(selector).is_checked()
