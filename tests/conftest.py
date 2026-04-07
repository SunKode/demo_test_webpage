from __future__ import annotations

from typing import Dict, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Yield a headless Firefox WebDriver and quit it after the test."""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    drv = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


@pytest.fixture
def pages(driver: WebDriver) -> Dict[str, object]:
    """Return a dict of page-object instances sharing the same driver."""
    return {
        "login": LoginPage(driver),
        "inventory": InventoryPage(driver),
        "cart": CartPage(driver),
        "checkout": CheckoutPage(driver),
    }
