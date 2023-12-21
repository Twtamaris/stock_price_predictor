import requests
from bs4 import BeautifulSoup
import csv

url = 'https://example.com/GBIME-price-history'

# Fetch the webpage
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find and extract price history data
price_history = []

# Assuming the price history is in a table, find the table element
table = soup.find('table')

# Assuming rows in the table contain price history data
rows = table.find_all('tr')

for row in rows:
    # Extract each cell in the row
    cells = row.find_all('td')
    # Process the cells to extract the data you need
    # Append data to price_history list

# Write data to a CSV file
with open('GBIME_price_history.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(price_history)
