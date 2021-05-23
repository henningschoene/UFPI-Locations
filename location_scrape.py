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

# Create list to hold all location dictionaries
all_locations = []

# Loop over all locations
for result in results:
    # extract details for individual location into location_dict
    name = result.find(class_='result-card__title').text
    street = result.find(class_='field-street-address').text
    city = result.find(class_='field-city').text.rstrip(', ')
    zip = result.find(class_='field-zip').text
    state = result.find(class_='field-state-abbreviation').text

    location_dict = {'name': name, 'street': street, 'city': city, 'zip': zip, 'state': state}
    # Append location_dict to all_locations
    all_locations.append(location_dict)

print(all_locations)

# Close webdriver
driver.quit()
