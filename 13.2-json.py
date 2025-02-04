"""
Welcome Hasan Faisal from Using Python to Access Web Data

Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2151237.json (Sum ends with 37)
"""
import urllib.request
import json

try:
    #url = input('Enter location: ')
    url = 'http://py4e-data.dr-chuck.net/comments_2151237.json'
except:
    print('Invalid URL')
    quit()

print(f'Retrieving {url}')

# Reading the data from URL
response = urllib.request.urlopen(url)
data = response.read().decode()


# Parse the JSON data
info = json.loads(data)
print(type(info))
print(info)

print('User count:', len(info))

list = []

if 'comments' in info:
    for item in info['comments']:
        # print('Name', item['name'])
        # print('Id', item['count'])

        list.append(item['count'])

print('Sum:', sum(list))