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

# Integer that counts if there are exactly two of the same character in box_id
pairs = 0
pairs_in_loop = 0

# Integer that counts if there are exactly three of the same character in box_id
three_of_a_kind = 0
three_of_a_kind_in_loop = 0

# Loop through all box ID's
for box_id in box_ids:
    for character in box_id:

        # Holds the amount of characters of a certain type in box_id
        amount_of_that_character = box_id.count(character)
        if amount_of_that_character == 2:
            pairs_in_loop += 1
        if amount_of_that_character == 3:
            three_of_a_kind_in_loop += 1

    # If we found pairs or three of a kind, add one to the counter and reset in loop counter
    if pairs_in_loop > 0:
        pairs_in_loop = 0
        pairs += 1
    if three_of_a_kind_in_loop > 0:
        three_of_a_kind_in_loop = 0
        three_of_a_kind += 1

print('Total sum : {}'.format(pairs * three_of_a_kind))
