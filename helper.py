from bs4 import BeautifulSoup
import requests
import json

# get the html doc for the data i need
doc = requests.get('https://www.computerhope.com/issues/ch001789.htm')

# get the beautiful soup object
soup = BeautifulSoup(doc.text, 'html.parser')

# find all the relevant headings
headings = soup.find_all('h2')

# starter dictionary for later conversion to json format
my_data = {}

# iterate over all headings in the headings list (relevant ones)
for item in headings[:-1]:

    # get the unordered list that immediately follows the heading - creates a ul tag
    list_ext = item.find_next_sibling('ul')

    # all the extension names are stored in bold tags. hence to find all instances of "b" in the ul tag
    exts = list_ext.find_all('b')

    # create my data keys - with the first word of the heading, with the keys as a list of extension names stored
    # as strings
    my_data[item.contents[0].split(' ')[0]] = [ext.text for ext in exts]

# writing a json file
with open('extensions.json', 'w') as extensions:
    json_data = json.dumps(my_data, indent=2)
    extensions.write(json_data)

