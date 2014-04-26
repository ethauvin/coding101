#!/usr/bin/env python

# Coding 101
# 
# Written by Erik C. Thauvin (erik@thauvin.net)
# http://erik.thauvin.net/
# http://github.com/ethauvin/coding101/episode14
# April 26, 2014

import textwrap

# Print opening title
print "================================ CODING 101 ================================"

# Open the file
episodeFile = open("coding101.txt", "r")
# Read the lines into a list
linesFromFile = episodeFile.readlines()
# Close the file
episodeFile.close()

# Let's go. The program will execute until run = False
run = True
while run:
    # Print an empty line
    print
    # Print the episode list
    print "Choose an episode:"
    print

    # Loop through the episodes list.
    count = 0
    for line in linesFromFile:
        # Increment the episode number.
        count += 1
        # Split the line using tab as the delimiter
        # The format is: Date<TAB>Episode Title<TAB>Description
        episode = line.split("\t")
        # Print the episode number & title.
        # The episode number is converted into a str, and right justified
        print "\t{0}. {1}".format(str(count).rjust(2), episode[1])

    print

    # Ask for the episode number
    choice = raw_input("Enter 0-" + str(count) + " (or ENTER to quit): ")

    # Did you press enter?
    if not choice:
        # Stop the program execution. Bye-Bye!
        run = False

    # Validate the selected episode number. It must be a number...
    elif choice.isdigit():
        # Convert the selection to an integer.
        selection = int(choice)

        # It must also be between 1 and the total number of episodes
        # Could be written as: selection >= 1 and selection <= count
        if 1 <= selection <= count:
            print
            print
            print "============================================================================"
            # Get and split the line for the episode, the list is zero-based.
            episode = linesFromFile[selection - 1].split('\t')
            # Print the episode, title
            print "Episode #" + choice + ": \"" + episode[1] + '" aired on ' + episode[0]
            print
            # Print the description, using textwrap to make it look pretty.
            print textwrap.fill(episode[2], width=76)
            print "============================================================================"
            print
            raw_input("Press ENTER to continue...")
