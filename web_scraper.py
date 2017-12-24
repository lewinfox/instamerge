# Scrape Instagram for images
from bs4 import BeautifulSoup
import requests

tag = str.lower(input("Enter your hashtag: \n"))
url = "http://www.instagram.com/tags/{}".format(tag)
print("Searching " + url)

# Retrieve URL data
page = requests.get(url)
print("Requests status code {}".format(page.status_code))

# Convert to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')
# Extract body
body = soup.body
