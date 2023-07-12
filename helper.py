from bs4 import BeautifulSoup
import requests
import os.path
import json

DATA_FILE = './extensions.json'


def get_json_data():
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
    with open(DATA_FILE, 'w') as extensions:
        json_data = json.dumps(my_data, indent=2)
        extensions.write(json_data)


# get file extension function
def get_extension(filename):
    if '.' in filename:
        # get the last occurrence of '.' in the string and splice the string accordingly
        extension = filename[filename.rindex('.'):]
        # return the spliced string
        return extension
    else:
        return None


# Create a new filename if a file with same name exists already
def new_filename(filepath, filename, copy_num=1):

    # Check if the file already exists, and if it does:
    if os.path.exists(fr"{filepath}\{filename}"):
        # Create a new name to recursively search
        x = filename.split('.')
        if len(x) > 1:
            temp_altered_name = ''.join([part for part in x[:-1]]) + f'({copy_num}).{x[-1]}'
        else:
            temp_altered_name = x[0]+f'({copy_num})'

        # return the new name
        return new_filename(filepath, temp_altered_name, copy_num=copy_num + 1)

    # return the original name if file does not exist
    else:
        return fr"{filepath}\{filename}"


# run only when used as a module
if __name__ == 'helper':
    # to check if the extension file is already present, because if so, not required to create again
    if not os.path.isfile(DATA_FILE):
        get_json_data()
        print(f'JSON Data File created at {os.path.abspath(DATA_FILE)}')

    else:
        print(f'File with filepath with {os.path.abspath(DATA_FILE)} already exists. Have not created new data.')