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


# Loop through all box ID's
for box_id in box_ids:

    # Get diff between the current and previous string
    difflib.ndiff()
