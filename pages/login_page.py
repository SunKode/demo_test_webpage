from __future__ import annotations

from typing import Optional

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.credentials import get_password

URL = "https://www.saucedemo.com/"


class LoginPage(BasePage):
    def open(self) -> LoginPage:
        """Navigate to the login page and return self for chaining."""
        self.driver.get(URL)
        return self

    def login(self, username: str, password: Optional[str] = None) -> None:
        """Enter credentials and submit the login form."""
        self.type_into(By.ID, "user-name", username)
        self.type_into(By.ID, "password", password or get_password())
        self.find(By.ID, "login-button").click()

    def error_message(self) -> str:
        """Return the login error message text."""
        return self.find(By.CSS_SELECTOR, "[data-test='error']").text
