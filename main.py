import os
import json
import helper
import data_editor

action = input("C for cleaning a directory or E for editing the dataset: \n").lower()

if action == 'c':
    FOLDER_TO_CLEAN = input("Please give an absolute filepath, such as C:\\Users\\kevin\\Downloads\\Personal :\n")

    items = os.listdir(FOLDER_TO_CLEAN)

    with open(helper.DATA_FILE, 'r') as data:
        ext_dict = json.load(data)

    for item in items:
        src_file_name_path = fr'{FOLDER_TO_CLEAN}\{item}'

        if os.path.isfile(src_file_name_path):
            item_extension = helper.get_extension(item)

            for key, value in ext_dict.items():
                if item_extension in value:
                    dest_filepath = fr'{FOLDER_TO_CLEAN}\{key}'
                    os.makedirs(dest_filepath, exist_ok=True)

                    dest_file_name_path = helper.new_filename(dest_filepath, item)

                    os.rename(src_file_name_path, dest_file_name_path)

elif action == 'e':
    data_editor.edit_json()
