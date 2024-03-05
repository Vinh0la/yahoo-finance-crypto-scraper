from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

root = "https://finance.yahoo.com/crypto/"
path = r"C:\Python Files\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(path))
wait = WebDriverWait(driver, 10)

name = []
price = []
change = []
circulating_supply = []
volume = []

num = 0
batch_size = 25

while num <= 8975:
    pages = f"{root}?count={batch_size}&offset={num}"
    driver.get(pages)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//table//tbody//tr')))
    table_data = driver.find_elements(By.XPATH, '//table//tbody//tr')

    for data in table_data:
        columns = data.find_elements(By.TAG_NAME, 'td')
        name.append(columns[1].text)
        price.append(columns[2].text)
        change.append(columns[3].text)
        volume.append(columns[7].text)
        circulating_supply.append(columns[9].text)

    num += batch_size

df = pd.DataFrame({'Name': name, 'Price': price, 'Change':change, 'Volume in Currency':volume, 'Circulating Supply': circulating_supply})
df.to_csv('Top 500 Crypto.csv', index=False)

driver.quit()
