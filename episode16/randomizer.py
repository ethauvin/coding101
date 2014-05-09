#!/usr/bin/env python

# Coding 101: Randomizer
# 
# Written by Erik C. Thauvin (erik@thauvin.net)
# http://erik.thauvin.net/
# http://github.com/ethauvin/coding101/
# May 9, 2014

# Import the randrange function
# See: http://www.tutorialspoint.com/python/number_randrange.htm
from random import randrange

# The maximum number of random numbers to generate
max = 100
# The name of the file to write the number to
fileName = 'random.txt'

# Initialize the list of random numbers
randomNumbers = []

print
print 'Generating ' + str(max) + ' random numbers...'
print

# Initialize the print counter
printCounter = 0
# Loop until we have 100 random numbers in our list
while len(randomNumbers) < max:
    # Get a random number between 0 and 100
    randint = randrange(max)
    # Append the random number to our list
    randomNumbers.append(randint)
    # Print the random number, converted to a string and right justified
    # See: http://www.tutorialspoint.com/python/string_rjust.htm
    # The comma at the end prevents a new line from being printed
    print '  ' + str(randint).rjust(2),
    # Increment the print counter, same as: printCounter = printerCounter + 1
    printCounter += 1
    # If the print counter is 10, print a new line, and reset the counter
    if printCounter == 10:
        print
        printCounter = 0

print
raw_input('Press ENTER to continue...')

print
print 'Sorting...'
print

# Sort the numbers
randomNumbers.sort()

# Open the file for writing, it will be closed automatically when done
with open(fileName, 'w') as f:
    printCounter = 0
    # Loop through our random number list.
    for number in randomNumbers:
        # Write the number to the file, followed by a new line
        f.write(str(number) + '\n')
        # Also print the number on screen
        print '  ' + str(number).rjust(2),
        printCounter += 1
        if printCounter == 10:
            print
            printCounter = 0

print
print 'The numbers have been written to "' + fileName + '"'
print

raw_input('Press ENTER to quit...')