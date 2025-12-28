from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

list_dict = {}
time_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li time")
name_list = driver.find_elements(By.CSS_SELECTOR,".event-widget ul li a")

for i in range(0,5):
    list_dict[i] = {
        "time": time_list[i].text,
        "name": name_list[i].text,
    }
print(list_dict)

driver.close()



