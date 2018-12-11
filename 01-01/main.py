#
# Solution for advent of code 2018 01/12 puzzle 1
#

# Get the three frequencies from user, as  integers
frequency_1 = int(input("Frequency #1 : "))
frequency_2 = int(input("Frequency #2 : "))
frequency_3 = int(input("Frequency #3 : "))

# Calculate the resulting frequency
resulting_frequency = (frequency_1 + frequency_2 + frequency_3)

# Output resulting frequency
print("The resulting frequency is : {}".format(resulting_frequency))
