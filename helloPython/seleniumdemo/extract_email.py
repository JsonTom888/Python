from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://home.baidu.com/contact.html")
doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+',doc)

for email in emails:
    print(email)

driver.quit()