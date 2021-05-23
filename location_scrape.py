import requests


locations_url = 'https://www.ufpi.com/en/our-locations'

locations = requests.get(locations_url)

print(locations)
