from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME,"fName")
first_name.send_keys("Madhu")

last_name = driver.find_element(By.NAME,"lName")
last_name.send_keys("Kiran")

email = driver.find_element(By.NAME,"email")
email.send_keys("madhukiran@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()