#!/usr/bin/env python

# Coding 101: RSVP
#
# Written by Erik C. Thauvin (erik@thauvin.net)
# http://erik.thauvin.net/
# http://github.com/ethauvin/coding101/
# May 18, 2014

# The name and extension of the file containing the RSVP list
file_name = 'rsvp'
file_ext = '.txt'

# The RSVP statuses
status_yes = 'Yes'
status_no = 'No'
status_nr = 'Not Replied'

# Print the banner
print '=================================== RSVP ====================================='

# Initialize the RSVP list
rsvp_list = []
# Read the file, line by line
for line in open(file_name + file_ext):
    # Append the split line as a tuple to our list
    # The file format is: name,status
    # e.g.: Shannon Morse,Yes
    # See: http://www.tutorialspoint.com/python/string_split.htm
    #      http://www.tutorialspoint.com/python/string_strip.htm
    #      http://www.tutorialspoint.com/python/python_tuples.htm
    rsvp_list.append(tuple(line.strip().split(',', 1)))

# Sort the list by names
rsvp_list.sort(key=lambda rsvp: rsvp[0])


#
# Function to save the list based on the specified status
#
def save_list(status):
    # Create a new file using the status
    # e.g: rsvp-yes.txt, rsvp-no.txt, rsvp-not-replied.txt
    # See: http://www.tutorialspoint.com/python/string_replace.htm
    #      http://www.tutorialspoint.com/python/string_lower.htm
    new_file = file_name + '-' + status.replace(' ', '-').lower() + file_ext
    # Open the file for writing, it will be closed automatically when done
    with open(new_file, 'w') as f:
        # Loop through the RSVP list
        for rsvp in rsvp_list:
            # Determine if the line should be saved, by comparing its status
            # The statuses are all lower-cased, so the comparison is case-insensitive
            is_save = False
            if status.lower() == rsvp[1].lower() == status_yes.lower():
                is_save = True
            elif status.lower() == rsvp[1].lower() == status_no.lower():
                is_save = True
            elif status.lower() == rsvp[1].lower() == status_nr.lower():
                is_save = True

            if is_save:
                # Write the name, followed by a new line
                f.write(rsvp[0] + '\n')
    print
    print 'The list have been written to "' + new_file + '"'
    print


#
# Function to display the list based on the specified status, if any
#
def display_list(status=None):
    # Print the columns header
    print
    print ' #  Name                                                                  RSVP'
    print '=============================================================================='
    # The displayed line count
    count = 1
    for rsvp in rsvp_list:
        # Determine if the line should be displayed by comparing its status
        is_print = False
        if status is None:
            is_print = True
        elif status.lower() == rsvp[1].lower() == status_yes.lower():
            is_print = True
        elif status.lower() == rsvp[1].lower() == status_no.lower():
            is_print = True
        elif status.lower() == rsvp[1].lower() == status_nr.lower():
            is_print = True

        if is_print:
            # Print the count, name and status using right and left justification
            # See: http://www.tutorialspoint.com/python/string_rjust.htm
            #      http://www.tutorialspoint.com/python/string_ljust.htm
            #      http://www.tutorialspoint.com/python/string_title.htm
            print '{0}. {1} {2}'.format(str(count).rjust(2), rsvp[0].title().ljust(58), rsvp[1].title().rjust(15))
            # Increment the count, same as: count = count + 1
            count += 1
    print

    # Present the option to save the list to a file, is the status is specified
    if status is not None:
        save = raw_input('Type \'s\' to save or ENTER to continue: ')
        if save == 's':
            save_list(status)
    else:
        raw_input('Press ENTER to continue...')

#
# Let's go. The program will execute until run = False
#
run = True
while run:
    # Print the options
    print
    print 'Choose an option:'
    print
    print '\t1. RSVP: All'
    print '\t2. RSVP: ' + status_yes
    print '\t3. RSVP: ' + status_no
    print '\t4. RSVP: ' + status_nr
    print
    choice = raw_input('Enter option (or ENTER to quit): ')

    # Did you press enter?
    if not choice:
        # Stop the program execution. Bye-Bye!
        run = False

    # Validate the selected option. It must be a number...
    elif choice.isdigit():
        # Convert the selected option to an int
        selection = int(choice)
        # Display the list based on the selected status
        if selection == 1:
            display_list()
        elif selection == 2:
            display_list(status_yes)
        elif selection == 3:
            display_list(status_no)
        elif selection == 4:
            display_list(status_nr)