# demo_interviu — Selenium E2E Test Suite

End-to-end test suite for [SauceDemo](https://www.saucedemo.com/) built with **Selenium**, **pytest**, and the **Page Object Model** pattern.

---

## Project Structure

```
demo_interviu/
├── pages/
│   ├── base_page.py        # Shared WebDriver helpers
│   ├── login_page.py       # Login page interactions
│   ├── inventory_page.py   # Product listing page interactions
│   ├── cart_page.py        # Shopping cart page interactions
│   └── checkout_page.py    # Checkout flow interactions
├── tests/
│   ├── conftest.py         # pytest fixtures (driver, pages)
│   └── test_order.py       # All test cases
├── utils/
│   └── credentials.py      # Encrypted credential helpers
├── .env                    # Environment variables (not committed)
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.9+
- Firefox browser installed
- [GeckoDriver](https://github.com/mozilla/geckodriver) (managed automatically via `webdriver-manager`)

---

## Setup

1. Clone the repository and create a virtual environment:

```bash
git clone <repo-url>
cd demo_interviu
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:

```env
FERNET_KEY=<your_fernet_key>
PASSWORD=<fernet_encrypted_password>

STANDARD_USER=standard_user
LOCKED_OUT_USER=locked_out_user
PERFORMANCE_GLITCH_USER=performance_glitch_user
```

> The password is encrypted with [Fernet](https://cryptography.io/en/latest/fernet/) symmetric encryption.  
> To generate a key and encrypt your password:
> ```python
> from cryptography.fernet import Fernet
> key = Fernet.generate_key()
> token = Fernet(key).encrypt(b"your_password")
> ```

---

## Running Tests

Run the full suite:

```bash
pytest tests/
```

Run a specific test:

```bash
pytest tests/test_order.py::test_complete_order_standard_user
```

Run with verbose output:

```bash
pytest tests/ -v
```

---

## Test Cases

| # | Test | Description |
|---|------|-------------|
| 1 | `test_complete_order_standard_user` | Full happy-path order flow |
| 2 | `test_locked_out_user_cannot_login` | Locked-out user sees error message |
| 3 | `test_multiple_items_order` | Add 2 items, verify badge, complete order |
| 4 | `test_empty_cart_has_no_items` | Cart is empty before adding items |
| 5 | `test_checkout_requires_first_name` | Form validation — missing first name |
| 6 | `test_checkout_requires_last_name` | Form validation — missing last name |
| 7 | `test_checkout_requires_zip_code` | Form validation — missing postal code |
| 8 | `test_order_summary_shows_correct_item` | Order summary matches added item |
| 9 | `test_complete_order_performance_glitch_user` | Glitch user can still complete order |
| 10 | `test_cancel_checkout_returns_to_cart` | Cancel on step-one returns to cart |
| 11 | `test_cancel_order_overview_returns_to_inventory` | Cancel on step-two returns to inventory |
| 12 | `test_remove_item_from_cart` | Removing item empties the cart |

---

## Notes

- Tests run in **headless Firefox** by default.
- The `pages` fixture in `conftest.py` provides all page objects sharing a single driver instance per test.
- `.env` is excluded from version control — never commit credentials.

---

## Last Test Run

```
platform win32 -- Python 3.13.5, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\vladi\PycharmProjects\demo_test_webpage
collected 12 items

tests\test_order.py ............                                                                                                            [100%]

========================================================= 12 passed in 134.01s (0:02:14) =========================================================
```
