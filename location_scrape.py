from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Create firefox browser for selenium
opts = webdriver.FirefoxOptions()
# Turn headless browser on (True) or off (False)
opts.headless = False
driver = webdriver.Firefox(options=opts)
driver.set_page_load_timeout(30)

# Set start_url to scrape
url = 'https://www.ufpi.com/en/our-locations#location_e='

# Create list to hold all location dictionaries
all_locations = []

# Loop through all location pages (10 locations per page)
for start_number in range(0, 130, 10):
    # Open and parse url
    driver.get(url + str(start_number))
    # Wait 5 seconds between requests
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print(url + str(start_number))

    # Find each search result
    results = soup.find_all(class_='location-card')

    # Loop over all locations
    for result in results:
        # Extract details for individual location into location_dict
        name = result.find(class_='result-card__title').text
        street = result.find(class_='field-street-address').text
        city = result.find(class_='field-city').text.rstrip(', ')
        zip = result.find(class_='field-zip').text
        state = result.find(class_='field-state-abbreviation').text

        print(name)

        # Save location data in location_dict
        location_dict = {'name': name, 'street': street, 'city': city, 'zip': zip, 'state': state}
        # Append location_dict to all_locations
        all_locations.append(location_dict)

    # Wait 5 seconds between requests
    time.sleep(5)

print(all_locations)

# Close webdriver
driver.quit()
