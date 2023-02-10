from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.maximize_window()
driver.get('https://demoqa.com/tool-tips ')

greenBtn = driver.find_element(By.ID, 'toolTipButton')
textBox = driver.find_element(By.ID, 'toolTipTextField')
blueText = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/a[1]')

actions = ActionChains(driver)
actions.move_to_element(greenBtn)
actions.move_to_element(textBox)
actions.move_to_element(blueText)
actions.perform() # akan dieksekusi juka sudah sampai line "perform". jadi 1 kesatuan.

time.sleep(3)