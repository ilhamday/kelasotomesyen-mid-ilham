from selenium import webdriver

driver = webdriver.Chrome()

# List url yang perlu diakses
Urls = ["tiket.com", "tokopedia.com", "orangsiber.com", "demoqa.com", "automatetheboringstuff.com"]


for Url in Urls:
    driver.minimize_window()    # minimize window sejak awal
    driver.get(f"https://{Url}") # akses ke url yang sudah ditentukan
    Title = driver.title # menyimpan title website ke variable Title
    print(f"{Url} - {Title}")  # Url dari list + Title yang didapatkan

driver.close() # keluar dari window