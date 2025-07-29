# blinkit_bot.py
import asyncio
from playwright.sync_api import sync_playwright


def search_blinkit(item_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Show browser
        page = browser.new_page()
        page.goto("https://blinkit.com")

        # Wait for page to load and click search
        page.wait_for_selector('input[type="text"]')
        search_box = page.locator('input[type="text"]')
        search_box.fill(item_name)
        search_box.press('Enter')

        # Wait for results to load
        page.wait_for_timeout(4000)  # wait 4 seconds

        # Try to scrape the first product info
        try:
            product_name = page.locator('div.sc-dBaXSw.iJzfGp span').first.inner_text()
            price = page.locator('div.sc-jrcTuL.gxMbem span').first.inner_text()
            print(f"✅ Top Result for '{item_name}':")
            print(f"Name: {product_name}")
            print(f"Price: {price}")
        except:
            print(f"❌ Could not find product for: {item_name}")

        browser.close()


# Test
if __name__ == "__main__":
    item = "Amul butter"
    search_blinkit(item)

if __name__ == "__main__":
    grocery_list = [
        {"item": "Amul butter", "quantity": "2 packs", "brand": "Amul"},
        {"item": "basmati rice", "quantity": "1kg", "brand": "None"}
    ]

    for product in grocery_list:
        search_blinkit(product["item"])


from playwright.sync_api import sync_playwright

import re

def extract_numeric_price(price_str):
    match = re.search(r"\d+", price_str.replace(",", ""))
    return int(match.group()) if match else 0

def search_blinkit(item_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://blinkit.com")

        page.wait_for_selector('input[type="text"]')
        search_box = page.locator('input[type="text"]')
        search_box.fill(item_name)
        search_box.press('Enter')
        page.wait_for_timeout(4000)

        try:
            product_name = page.locator('div.sc-dBaXSw.iJzfGp span').first.inner_text()
            price_text = page.locator('div.sc-jrcTuL.gxMbem span').first.inner_text()
            price_numeric = extract_numeric_price(price_text)

            browser.close()
            return {
                "item": item_name,
                "product_name": product_name,
                "price": price_text,
                "price_numeric": price_numeric
            }
        except:
            browser.close()
            return {
                "item": item_name,
                "product_name": "Not found",
                "price": "N/A",
                "price_numeric": 0
            }
