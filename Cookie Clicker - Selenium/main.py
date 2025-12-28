import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
driver.maximize_window()

time.sleep(3)

print("Looking for language selection...")
try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    time.sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")

time.sleep(2)


start_time = time.time()
end_time = start_time + 360.0

button = driver.find_element(By.ID, value='bigCookie')
while start_time < end_time:
    button.click()
    if time.time() - start_time >= 10:
        try:
            list_enabled = driver.find_elements(By.CSS_SELECTOR, value='.storeSection .enabled')
            if len(list_enabled) > 0:
                list_enabled[-1].click()
        except NoSuchElementException:
            print("No Upgrade Available")
        start_time = time.time()

per_second = driver.find_element(By.ID, value='cookiesPerSecond').text
print(per_second)