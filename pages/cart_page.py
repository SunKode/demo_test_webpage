from __future__ import annotations

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class CartPage(BasePage):
    def items(self) -> List[WebElement]:
        """Return all cart item elements."""
        return self.find_all(By.CLASS_NAME, "cart_item")

    def remove_first_item(self) -> None:
        """Click the remove button on the first cart item."""
        self.find(By.CSS_SELECTOR, ".cart_item button").click()

    def proceed_to_checkout(self) -> None:
        """Click the checkout button to proceed to checkout."""
        self.find(By.ID, "checkout").click()
