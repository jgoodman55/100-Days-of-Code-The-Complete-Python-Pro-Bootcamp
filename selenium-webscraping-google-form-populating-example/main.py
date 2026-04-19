#%%
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone"
GOOGLE_FORM = "https://forms.gle/UFFPE1hV5qDkmfTZ7"

# ── Scraping ──────────────────────────────────────────────────────────────────

def fetch_with_retry(url, retries=5, backoff=2):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                raise
            print(f"Retrying in {backoff}s...\n")
            time.sleep(backoff)

def get_link(data):
    return data.find(name="a").get("href")

def get_address(data):
    address = data.find(name="address").getText()
    if "|" in address:
        address = address.split(" | ")[1].strip().replace("\n", "")
    else:
        address = address.split(",", maxsplit=1)[1].strip().replace("\n", "")
    return address

def get_price(data):
    price_text = data.find(
        name="span", class_="PropertyCardWrapper__StyledPriceLine"
    ).getText()
    match = re.search(r"\$\d{1,3}(?:,\d{3})*", price_text)
    return match.group() if match else "N/A"

# ── Selenium ──────────────────────────────────────────────────────────────────

def create_driver(headless=False):
    """Create a single reusable Chrome driver."""
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Suppress 'Chrome is being controlled by automated software' bar
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=options)

def fill_and_submit_form(driver, wait, property_info):
    """
    Navigate to the form, fill every text input, then click Submit.
    Returns True on success, False if something went wrong.
    """
    driver.get(GOOGLE_FORM)

    # Wait until the inputs are visible and the page is interactive
    input_boxes = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, 'input[type="text"]')
        )
    )

    for box, value in zip(input_boxes, property_info):
        box.click()
        box.clear()           # clear any leftover text from prior run
        box.send_keys(value)

    # Target the submit button specifically by its aria-label.
    # Google Forms renders it as: <div role="button" aria-label="Submit">
    # This avoids accidentally clicking Back/Next buttons.
    submit_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@role="button" and @aria-label="Submit"]')
        )
    )
    submit_btn.click()

    # Wait for the confirmation page so we know the submission went through
    # before moving on to the next property.
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[contains(text(), "Your response has been recorded")]')
        )
    )
    return True

# ── Main ──────────────────────────────────────────────────────────────────────

response = fetch_with_retry(ZILLOW_URL)
soup = BeautifulSoup(response.text, "html.parser")
wrapped_data = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper")
property_list = [
    (get_address(d), get_price(d), get_link(d)) for d in wrapped_data
]

print(f"Found {len(property_list)} properties. Submitting forms...\n")

# Create ONE driver and reuse it for every submission
driver = create_driver(headless=False)   # flip to True to run invisibly
wait   = WebDriverWait(driver, 15)       # slightly generous timeout

try:
    for i, info in enumerate(property_list, 1):
        print(f"[{i}/{len(property_list)}] {info[0]} — {info[1]}")
        try:
            fill_and_submit_form(driver, wait, info)
            print("  ✓ Submitted")
        except Exception as e:
            print(f"  ✗ Failed: {e}")
        time.sleep(1)   # polite pause between submissions
finally:
    driver.quit()       # always close the browser, even on crash

print("\nDone.")
# %%