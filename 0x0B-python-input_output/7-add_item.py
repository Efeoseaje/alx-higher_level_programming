#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Get the arguments passed to the script
args = sys.argv[1:]

# Load the existing list from the JSON file, if it exists
try:
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_list = []

# Add the arguments to the existing list
for arg in args:
    existing_list.append(arg)

# Save the updated list to the JSON file
save_to_json_file(existing_list, 'add_item.json')
