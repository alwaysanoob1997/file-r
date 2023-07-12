from bs4 import BeautifulSoup
import requests
import json

# get the html doc for the data i need
doc = requests.get('https://fileinfo.com/filetypes/common')

# get the beautiful soup object
soup = BeautifulSoup(doc.text, 'html.parser')

# find all the relevant headings
headings = soup.find_all('h2')

# starter dictionary for later conversion to json format
my_data = {}

# iterate over all headings in the headings list (relevant ones)
for item in headings:

    # get the div that immediately follows the heading - creates a div tag
    list_ext = item.find_next_sibling('div')

    # all the extension names are stored in a tags. hence to find all instances of "a" in the div tag
    exts = list_ext.find_all('a')

    # create my data keys - with the first word of the heading, with the keys as a list of extension names stored
    # as strings
    my_data[item.contents[0]] = [ext.text.lower() for ext in exts]

# writing a json file
with open('extensions.json', 'w') as extensions:
    json_data = json.dumps(my_data, indent=2)
    extensions.write(json_data)

