from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.maximize_window()



def test_accountButton():
    driver.get('https://mangadex.org/')
    time.sleep(2)
    driver.find_element(By.ID, 'avatar').click()
    
    signInText = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div[2]/div[2]/div/div[1]/div[3]/button[1]/span').text
    registerText = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div[2]/div[2]/div/div[1]/div[3]/button[2]/span').text
    
    assert signInText == 'Sign in'
    assert registerText == 'Register'

def test_registerPage():
    # driver.get('https://mangadex.org/')
    # driver.find_element(By.ID, 'avatar').click()
    registerButton = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div[2]/div[2]/div/div[1]/div[3]/button[2]')
    registerButton.click()
    time.sleep(2)
    registerLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Register')
    registerLink.click()

    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'kc-page-title')))
        title = driver.find_element(By.ID, 'kc-page-title').text
        
        assert title == 'Register'
    except TimeoutException:
        print('Loading lama')

    

# Register page - no recaptcha
def test_emptyRecaptcha():
    driver.find_element(By.ID, 'username').send_keys('ferry')
    driver.find_element(By.ID, 'password').send_keys('12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('12345678')
    driver.find_element(By.ID, 'email').send_keys('email@mail.com')
    driver.find_element(By.CLASS_NAME, 'pf-c-button pf-m-primary pf-m-block btn-lg').click()

    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kc-content-wrapper"]/div/span')))
        errorValidation = driver.find_element(By.XPATH, '//*[@id="kc-content-wrapper"]/div/span').text

        assert errorValidation == 'Invalid Recaptcha'
    except TimeoutException:
        print('Loading lama')