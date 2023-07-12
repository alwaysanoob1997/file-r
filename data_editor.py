import json
import helper
import time


# function for editing the json dataset
def edit_json():
    with open(helper.DATA_FILE, 'r') as file:
        data = json.load(file)

    action = input("F for adding a new filetype to a class, or C for making a new class: \n").lower()

    # Conditional for selecting action
    if action == 'f':
        add_filetype(data)

    elif action == 'c':
        add_class(data)


# Function for adding a filetype to an existing class
def add_filetype(data):
    # input for filetype
    new_filetype = input("Please mention the filetype as the example: '.mkv'\n").lower()
    # String conditional to make sure extensions have a '.' as the first character
    update = new_filetype if new_filetype.startswith('.') else '.' + new_filetype

    # make sure given extension is not already present in data
    for key, value in data.items():
        if update in value:
            print(f"Extension already present under {key}\n")
            exit(0)

    time.sleep(3)

    # Make sure class name matches something in list
    full_class = class_matcher(data)

    # Add to data
    data[full_class[0]].append(update)

    # write to file
    with open(helper.DATA_FILE, 'w') as extensions:
        json_data = json.dumps(data, indent=2)
        extensions.write(json_data)


def class_matcher(data):

    # Printing out existing classes
    print('Available classes:')
    print(*data, sep='\n')  # *data unpacks the list in the print function

    class_to_edit = input(f'Please select class to add extension to by name from above:\n').title()

    # list comprehension to select classes with only a substring entry
    full_class = [i for i in data if class_to_edit in i]

    # to restart the function if no matches found
    if len(full_class) < 1:
        print("Input does not match any Class. Please Try Again")
        time.sleep(3)
        class_matcher(data)
        exit(0)

    return full_class


# function to add new class
def add_class(data):
    new = input("Please give the name of the new class: \n").title()
    similar = [i for i in data if new in i]
    if len(similar) > 0:
        print(f"Similar class already exists \n {similar}")
        time.sleep(3)
        add_filetype(data)
        exit(0)

    # Add new entry to dictionary
    data[new] = []
    # adding a new filetype to newly created class
    add_filetype(data)


if __name__ == '__main__':
    pass
