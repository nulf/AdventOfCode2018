#
# Solution for advent of code 2018 01/12 puzzle 1
#


# Read the input file as a list
def read_input_file():
    input_file = open('input.txt', 'r')
    input_frequencies = input_file.read().splitlines()
    input_file.close()
    return input_frequencies


# Loop through all values in the list, if it's a positive value add it, otherwise subtract it
# Added for part 2 of puzzle 1 - find the first frequency we crunch twice
calculated_frequency = 0
first_frequency_crunched_twice = None
crunched_frequencies = []
input_frequencies = read_input_file()

while first_frequency_crunched_twice is None:
    for input_frequency in input_frequencies:
        if first_frequency_crunched_twice is None:
            if calculated_frequency in crunched_frequencies:
                first_frequency_crunched_twice = calculated_frequency
        crunched_frequencies.append(calculated_frequency)
        calculated_frequency = eval('calculated_frequency + int(input_frequency)')
    input_frequencies = read_input_file()

# Output resulting frequency
print("The resulting frequency is : {}".format(calculated_frequency))
print("First frequency we crunched twice : {}".format(first_frequency_crunched_twice))
