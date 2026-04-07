from __future__ import annotations

from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def fill_info(
        self,
        first: str = "Vlad",
        last: str = "Soare",
        zip_code: str = "55555",
    ) -> None:
        """Fill in the checkout form and click continue."""
        self.type_into(By.ID, "first-name", first)
        self.type_into(By.ID, "last-name", last)
        self.type_into(By.ID, "postal-code", zip_code)
        self.find(By.ID, "continue").click()

    def finish(self) -> None:
        """Wait for the order overview page and click finish."""
        self._wait.until(EC.url_contains("checkout-step-two"))
        self.find(By.ID, "finish").click()

    def cancel(self) -> None:
        """Click the cancel button on the current checkout step."""
        self.find(By.ID, "cancel").click()

    def confirmation_header(self) -> str:
        """Wait for the confirmation page and return the header text."""
        self._wait.until(EC.url_contains("checkout-complete"))
        return self.find(By.CSS_SELECTOR, "[data-test='complete-header']").text

    def summary_item_names(self) -> List[str]:
        """Return the list of item names shown on the order summary page."""
        self._wait.until(EC.url_contains("checkout-step-two"))
        return [el.text for el in self.find_all(By.CLASS_NAME, "inventory_item_name")]

    def error_message(self) -> str:
        """Return the validation error message text."""
        return self.find(By.CSS_SELECTOR, "[data-test='error']").text
