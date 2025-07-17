import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import sys

# PARAMETERS
COOKIES_FILE = "cookies.pkl"
CLASSES_ROW = "7"
WEEKDAY = "Wednesday" 
REGISTRATION_TIME = "21:30:00"

# Set up Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://crossfitgliwice.wod.guru/my-training")

# Load cookies
try:
    with open(COOKIES_FILE, "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
except Exception as e:
    print(f"❌ Error while loading cookies: {e}")
    sys.exit(1)

wait = WebDriverWait(driver, 10)

try:
    # Go to proper weekday
    for i in range(7):
        next_arrow = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/div/div/button[2]')))
        next_arrow.click()
        time.sleep(0.3)
    print(f"📅 Moved to: {WEEKDAY}")

    # Wait for registration time
    print(f"⏳ Waiting for {REGISTRATION_TIME}...")
    while datetime.now().strftime("%H:%M:%S") < REGISTRATION_TIME:
        time.sleep(0.1)

    print("🚀 21:30! Refreshing schedule...")
    
    # Refresh the schedule
    refresh_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-content-2"]/div/div/div/button')))
    refresh_button.click()
    print("🚀 Schedule refreshed")

    # Sign up for the class
    sign_up_button = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="tab-content-2"]/div/table/tbody/tr[{CLASSES_ROW}]/td[5]/button')))
    sign_up_button.click()
    confirm_sign_up_button = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="tab-content-2"]/div/table/tbody/tr[{CLASSES_ROW}]/td[5]/div[1]/button')))
    confirm_sign_up_button.click()
    print("✅ Signed up!")

except Exception as e:
    print(f"⚠️ Error occured: {e}")

finally:
    driver.quit()