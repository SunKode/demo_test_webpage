from __future__ import annotations

from typing import List, Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        """Initialise the page with a Selenium WebDriver instance."""
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)

    def find(self, by: str, value: str) -> WebElement:
        """Wait for and return a single element located by the given strategy."""
        return self._wait.until(EC.presence_of_element_located((by, value)))

    def find_all(self, by: str, value: str) -> List[WebElement]:
        """Return all elements matching the given locator strategy."""
        return self.driver.find_elements(by, value)

    def type_into(self, by: str, value: str, text: Optional[str]) -> None:
        """Clear and type text into the element located by the given strategy."""
        el = self.find(by, value)
        el.send_keys(text if text else "")

    @property
    def current_url(self) -> str:
        """Return the current browser URL."""
        return self.driver.current_url
