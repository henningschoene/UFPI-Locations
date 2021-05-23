from selenium import webdriver
from bs4 import BeautifulSoup

# Create firefox browser for selenium
opts = webdriver.FirefoxOptions()
# Turn headless browser on (True) or off (False)
opts.headless = True
driver = webdriver.Firefox(options=opts)
driver.set_page_load_timeout(30)

url = 'https://www.ufpi.com/en/our-locations'

# Open and parse url
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find each search result
results = soup.find_all(class_='location-card')

for result in results:
    name = result.find(class_='result-card__title').text
    street = result.find(class_='field-street-address').text
    city = result.find(class_='field-city').text.rstrip(', ')
    zip = result.find(class_='field-zip').text
    state = result.find(class_='field-state-abbreviation').text

    print(f'Name: {name}\nStreet: {street}\nCity: {city}\nZip: {zip}\nState: {state}\n')
