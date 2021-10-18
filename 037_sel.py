from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver_location = 'chromedriver.exe'
driver = webdriver.Chrome(driver_location)
driver.get('https://particle-clicker.web.cern.ch/')
driver.maximize_window()

clickable_object = driver.find_element('id', 'detector-events')

for a in range(0, 10):
    clickable_object.click()