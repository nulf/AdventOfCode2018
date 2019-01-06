#
# Solution for advent of code 2018 02/12 part 1
#


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
    for character in box_id:

        # Holds the amount of characters of a certain type in box_id
        amount_of_that_character = box_id.count(character)
