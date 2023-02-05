from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.maximize_window()
driver.get('https://demoqa.com/webtables')

# print(driver.find_elements(By.XPATH, '//span[@title="Delete"]'))

driver.find_element(By.ID, 'addNewRecordButton').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"registration-form-modal")))
driver.find_element(By.ID, 'firstName').send_keys('first1')
driver.find_element(By.ID, 'lastName').send_keys('last1')
driver.find_element(By.ID, 'userEmail').send_keys('nama1@mail.com')
driver.find_element(By.ID, 'age').send_keys('11')
driver.find_element(By.ID, 'salary').send_keys('100')
driver.find_element(By.ID, 'department').send_keys('CS')
driver.find_element(By.ID, 'submit').click()
