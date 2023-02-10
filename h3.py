from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.maximize_window()
driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID, 'promtButton').click()
driver.switch_to.alert.send_keys('hallo~')
driver.switch_to.alert.accept()

time.sleep(3)