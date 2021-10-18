from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_location = 'chromedriver.exe'
driver = webdriver.Chrome(driver_location)
driver.get('http://www.gammatest.net')
driver.maximize_window()

#link = driver.find_element('link text', 'Rohkem infot')
#link = driver.find_element('partial link text', 'Rohkem')
#link.click()
linkk = driver.find_element('partial link text', 'Rohkem')
linkk.click()

cells = driver.find_elements('tag name', 'td')
for a in cells:
    print(a.text)

#for a in link:
#   a.send_keys(Keys.CONTROL + Keys.RETURN)
#   time.sleep(3)


