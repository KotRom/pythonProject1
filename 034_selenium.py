# dpwnload web driver for chrome or firefox, copy to project folder
#https://sites.google.com/chromium.org/driver/
#pip install selenium
# pip install urllib3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import time

driver_location = 'chromedriver.exe'
driver = webdriver.Chrome(driver_location)
#print(driver.title)
driver.get('http://www.github.com')
#driver.maximize_window()
time.sleep(3)

search = driver.find_element_by_id('user_email')
#search = driver.find_element('id', 'user_email')
#print(search)
search.send_keys('rom@test.com')
search.send_keys(Keys.ENTER)
#print(driver.page_source)

time.sleep(5)
continue_button = driver.find_element('xpath', '/html/body/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/button')
continue_button.click()
password = driver.find_element('id', 'password')
password.send_keys('12345')
time.sleep(3)
password.clear()