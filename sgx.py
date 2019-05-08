import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Install geckodriver
#https://stackoverflow.com/questions/40867959/installing-geckodriver-only-using-terminal
# wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
# tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
# rm geckodriver-v0.11.1-linux64.tar.gz
# chmod +x geckodriver
# cp geckodriver /usr/local/bin/


# https://stackoverflow.com/questions/51046454/how-can-we-use-selenium-webdriver-in-colab-research-google-com
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Firefox(firefox_options=firefox_options)

url = "https://www2.sgx.com/securities/company-announcements"
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_class_name("sgx-button--primary").click()
loop = True
all_rows = []
try:
    while loop:
        print('.', end='', flush=True)
        driver.find_element_by_tag_name("table")
        res = driver.page_source
        soup = BeautifulSoup(res)
        all_rows.extend(soup.find_all("tr"))
        next_button = driver.find_element_by_class_name("sgx-pagination-next")
        next_button.click() # throws selenium.common.exceptions.ElementNotInteractableException if not present
except Exception:
    print(Exception)
driver.close()

# res = requests.get(url)
# soup = BeautifulSoup(res.content)

print(len(all_rows))
# remove header row
all_data = []
for r in all_rows:
    cols = r.find_all("td")
    if len(cols) > 0:
        row_data = []
        for c in cols:
            text = c.get_text()
            row_data.append(text)
        all_data.append(row_data)
import pdb; pdb.set_trace()
print('done!')
