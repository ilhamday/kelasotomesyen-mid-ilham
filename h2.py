from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')
driver.maximize_window()

driver.find_element(By.ID, 'userName').send_keys('I Ferry')
driver.find_element(By.ID, 'userEmail').send_keys('ferry@mail.com')
driver.find_element(By.ID, 'currentAddress').send_keys('alamat pribadi')
driver.find_element(By.ID, 'permanentAddress').send_keys('alaman permanent')
driver.find_element(By.ID, 'submit').click()

time.sleep(2)