# Load the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Add Link
Wiki_link = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
link = requests.get(Wiki_link).text

# Create BeautifulSoup object
soup = BeautifulSoup(link, 'html.parser')

# Find the right table
right_table = soup.find('table', class_="wikitable sortable")

# Find all links in the table
table_links = right_table.findAll('a')

# Extract country names from links
country = [link.get('title') for link in table_links]

# Create a DataFrame
pruthvi = pd.DataFrame()
pruthvi['Country'] = country

# Save DataFrame to a readme file
pruthvi.to_csv('readme.csv', index=False)
