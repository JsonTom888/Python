from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("https://www.baidu.com")
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium');
driver.find_element_by_xpath('//*[@id="su"]').click();
time.sleep(4)
a = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').is_displayed();
print(a)
ele_string = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').text
print(ele_string)
if (ele_string == u"Selenium automates browsers. That's it!"):
    print ("测试成功，结果和预期结果匹配！")

driver.quit()