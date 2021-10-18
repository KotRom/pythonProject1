# dpwnload web driver for chrome or firefox, copy to project folder
#pip install selenium
# pip install urllib3


from selenium import webdriver
import time

driver_location = 'chromedriver.exe'
driver = webdriver.Chrome(driver_location)
#print(driver.title)
driver.get('http://www.github.com')
time.sleep(5)

search = driver.find_element_by_id('user_email')
print(search)