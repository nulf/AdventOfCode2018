#
# Solution for advent of code 2018 02/12 part 1
#

import difflib


# Function for reading the input file as a list
def read_input_file():
    input_file = open('input.txt', 'r')
    input_box_ids = input_file.read().splitlines()
    input_file.close()
    return input_box_ids


# Read input file with box ID's
box_ids = read_input_file()

# List of previous box ID's
read_box_ids = []

# Loop through all box ID's
for box_id in box_ids:
    read_box_ids.append(box_id)

    # Get diff between the current and all previous box ID's
    for read_box_id in read_box_ids:
        print(difflib.ndiff(box_id, read_box_id))
