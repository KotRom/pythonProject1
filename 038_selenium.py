from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.youtube.com/channel/UCQo1k83IQy7eohMsJqpNYoQ/videos'
driver = webdriver.Chrome()

width = driver.get_window_size().get('width')
height = driver.get_window_size().get('height')
print(width, height)
# driver.set_window_size(250, 250)
pos_x = driver.get_window_position().get('x')
pos_y = driver.get_window_position().get('y')

print(pos_x, pos_y)
driver.set_window_position(200, 200)

driver.get(url)
agree_btn = driver.find_element('xpath', '')
agree_btn.click()

driver.save_screenshot('mai.png')

print(driver.current_url)

#driver.back()
#driver.forward()
#driver.refresh()
#print(driver.current_window_handle)
original_window = driver.currentwindow_handle
driver.switch_to.new_window('tab')
#driver.switch_to.new_window('window')
driver.get('http://www.github.com')
second_window = driver.current_window_handle

driver.switch_to.new_window('window')
print(original_window, second_window)
driver.switch_to.window(original_window)
time.sleep(3)
driver.switch_to.window(second_window)

