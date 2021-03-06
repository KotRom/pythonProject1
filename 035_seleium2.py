from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_location = 'chromedriver.exe'
driver = webdriver.Chrome(driver_location)
driver.get('http://www.github.net')
driver.maximize_window()

#WebDriverWait(driver, 10).until - zdjot max 10 sek do togo kak tol'ko element zagruzitca
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/h1'))
    )
    print(element.text)
except:
    print('Error')
