from selenium import webdriver
from bs4 import BeautifulSoup

# Create firefox browser for selenium
opts = webdriver.FirefoxOptions()
# Turn headless browser on (True) or off (False)
opts.headless = False
driver = webdriver.Firefox(options=opts)
driver.set_page_load_timeout(30)

url = 'https://www.ufpi.com/en/our-locations'

# Open and parse url
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find each search result
results = soup.find_all(class_='location-card')

# Print all search get_results
print(results)
