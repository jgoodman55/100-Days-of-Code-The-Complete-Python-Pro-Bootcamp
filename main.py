#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import time

# Set the duration in seconds (5 minutes * 60 seconds)
duration = 5 * 60
start_time = time.time()

URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Wait for the modal and find an element inside it
lang_select = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "langSelect-EN"))
)
lang_select.click()

big_cookie = WebDriverWait(driver, 2).until(
    EC.visibility_of_element_located((By.ID, "bigCookie"))
)

print("Loop started. It will run for 5 minutes.")
while time.time() - start_time < duration:
    big_cookie.click()
    wait = WebDriverWait(driver, timeout=5, poll_frequency=5)
    cookies = wait.until(EC.presence_of_element_located((By.ID, "cookies")))
    cookies_score = int(cookies.text.split(" ")[0])
    # driver.find_element(By.CLASS_NAME, "your-class-name")
    upgrades = driver.find_elements(by=By.CLASS_NAME, value="product.unlocked.enabled")
    try:
        best_upgrade_index = np.argmax([int(upgrade.find_element(By.CLASS_NAME, "price").text.replace(",", "")) for upgrade in upgrades])
        print(f"Best upgrade: {upgrades[best_upgrade_index].text}")
        upgrades[best_upgrade_index].click()
    except ValueError:
        pass

cookies_per_second = driver.find_element(by=By.ID, value="cookiesPerSecond").text.split(": ")[1]
print(f"cookies/second : {cookies_per_second}")
driver.quit()
# %%
