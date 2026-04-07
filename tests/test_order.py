from __future__ import annotations

from typing import Dict

from utils.credentials import get_user


def login(pages: Dict[str, object], user_key: str) -> None:
    """Open the login page and authenticate with the given user key."""
    pages["login"].open().login(get_user(user_key))


def test_complete_order_standard_user(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info()
    pages["checkout"].finish()
    assert "Thank you for your order" in pages["checkout"].confirmation_header()


def test_locked_out_user_cannot_login(pages):
    login(pages, "LOCKED_OUT_USER")
    assert "locked out" in pages["login"].error_message().lower()


def test_multiple_items_order(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item(0)
    pages["inventory"].add_item(1)
    assert pages["inventory"].cart_badge() == "2"
    pages["inventory"].go_to_cart()
    assert len(pages["cart"].items()) == 2
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info()
    pages["checkout"].finish()
    assert "Thank you for your order" in pages["checkout"].confirmation_header()


def test_empty_cart_has_no_items(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].go_to_cart()
    assert len(pages["cart"].items()) == 0


def test_checkout_requires_first_name(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info(first="")
    assert "first name" in pages["checkout"].error_message().lower()


def test_checkout_requires_last_name(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info(last="")
    assert "last name" in pages["checkout"].error_message().lower()


def test_checkout_requires_zip_code(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info(zip_code="")
    assert "postal code" in pages["checkout"].error_message().lower()


def test_order_summary_shows_correct_item(pages):
    login(pages, "STANDARD_USER")
    item_name = pages["inventory"].first_item_name()
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info()
    assert item_name in pages["checkout"].summary_item_names()


def test_complete_order_performance_glitch_user(pages):
    pages["login"].driver.implicitly_wait(15)
    login(pages, "PERFORMANCE_GLITCH_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info()
    pages["checkout"].finish()
    assert "Thank you for your order" in pages["checkout"].confirmation_header()


def test_cancel_checkout_returns_to_cart(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].cancel()
    assert "/cart.html" in pages["checkout"].current_url


def test_cancel_order_overview_returns_to_inventory(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].proceed_to_checkout()
    pages["checkout"].fill_info()
    pages["checkout"].cancel()
    assert "/inventory.html" in pages["checkout"].current_url


def test_remove_item_from_cart(pages):
    login(pages, "STANDARD_USER")
    pages["inventory"].add_item()
    pages["inventory"].go_to_cart()
    pages["cart"].remove_first_item()
    assert len(pages["cart"].items()) == 0
