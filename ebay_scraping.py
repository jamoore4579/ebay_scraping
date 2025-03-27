#Import Dependencies
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL for the eBay search
url = "https://www.ebay.com/sch/i.html"

# Define the query parameters for the search request
params = {
    '_from': 'R40',
    '_nkw': '/299 rookie', # Search Items
    '_udlo': '10', # Minimum price
    '_udhi': '30', # Maximym price
    '_sacat': 0, # Category ID
    '_sop': 1, # Sort Order ID
    'LH_Auction': 0, # Only Auction Listings
    'LH_BO': 1, # Accepts Offers
    'LH_FS': 1, # Only Free Shippings
    '_ipg': '240', # Number of items per page, Max is 240
    'rt': 'nc'
}

# Create a prepared request to inspect the full URL
request = requests.Request('GET', url, params=params)
prepared_request = request.prepare()
print(prepared_request.url)