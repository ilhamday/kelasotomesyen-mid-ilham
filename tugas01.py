from selenium import webdriver

driver = webdriver.Chrome()

Urls = ["tiket.com", "tokopedia.com", "orangsiber.com", "demoqa.com", "automatetheboringstuff.com"]

for x in Urls:
    driver.minimize_window()
    driver.get("https://{}".format(x))
    title = driver.title
    print(f"{x} - {title}")    

driver.close()