# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get the URL from the user
# url : http://py4e-data.dr-chuck.net/known_by_Morna.html
url = input('Enter URL: ')

# Number of times to follow the link
repeat_count = 7

# Position of the link to follow (1-based index)
position = 18

for i in range(repeat_count):
    print(f"Retrieving: {url}")  # Print the URL being accessed

    # Open the URL and parse the HTML
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor (<a>) tags
    tags = soup('a')

    # Ensure there are enough links on the page
    if len(tags) < position:
        print("Not enough links on the page!")
        break

    # Get the 18th link (0-based index is 17)
    url = tags[position - 1].get('href', None)

# Extract and print the final name from the last URL
name = url.split('_')[-1].split('.')[0]
print("Last retrieved name:", name)