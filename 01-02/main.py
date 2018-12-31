#
# Solution for advent of code 2018 01/12 puzzle 1
#

# Read the input file as a list
input_file = open('input.txt', 'r')
input_frequencies = input_file.read().splitlines()
input_file.close()


# Loop through all values in the list, if it's a positive value add it, otherwise subtract it
calculated_frequency = 0
for input_frequency in input_frequencies:
    calculated_frequency = eval('calculated_frequency + int(input_frequency)')


# Output resulting frequency
print("The resulting frequency is : {}".format(calculated_frequency))
