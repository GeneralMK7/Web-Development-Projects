import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

find_no_articles = driver.find_elements(By.CSS_SELECTOR,value='#articlecount ul li a')
print(find_no_articles[1].text)
# find_no_articles[1].click()

# open_media_wiki = driver.find_element(By.LINK_TEXT,value='MediaWiki')
# open_media_wiki.click()


search = driver.find_element(By.NAME,"search")
search.send_keys("Python",Keys.ENTER)

time.sleep(10)
driver.quit()
