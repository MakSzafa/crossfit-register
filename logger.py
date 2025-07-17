import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

# Logging data
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Set up Chrome options
options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://crossfitgliwice.wod.guru/user/login")
time.sleep(2)

# Login to the website
driver.find_element(By.NAME, "identity").send_keys(EMAIL)
driver.find_element(By.NAME, "credential").send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@id="login-button"]/button').click()

with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Cookies saved.")
driver.quit()