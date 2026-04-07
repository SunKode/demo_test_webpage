from __future__ import annotations

from typing import Optional

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def first_item_name(self) -> str:
        """Return the name of the first inventory item."""
        return self.find(By.CLASS_NAME, "inventory_item_name").text

    def add_item(self, index: int = 0) -> None:
        """Click the add-to-cart button for the item at the given index."""
        buttons = self.find_all(By.CSS_SELECTOR, ".inventory_item button")
        buttons[index].click()

    def cart_badge(self) -> Optional[str]:
        """Return the cart badge count text, or None if the badge is absent."""
        badges = self.find_all(By.CLASS_NAME, "shopping_cart_badge")
        return badges[0].text if badges else None

    def go_to_cart(self) -> None:
        """Click the shopping cart link to navigate to the cart page."""
        self.find(By.CLASS_NAME, "shopping_cart_link").click()
