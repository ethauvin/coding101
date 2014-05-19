#!/usr/bin/env python

# Coding YouTube 101
# 
# Written by Erik C. Thauvin (erik@thauvin.net)
# http://erik.thauvin.net/
# http://github.com/ethauvin/coding101/
# May 1, 2014

# To warp long lines
import textwrap
# For making http requests
import urllib2
# For decoding YouTube's API responses
import json

# Your YouTube API key from https://developers.google.com/youtube/registering_an_application
youtube_api_key = ''

# Print opening title
print '============================= CODING YOUTUBE 101 ============================='
# Print an empty line
print

# Ask for the API key if none is specified above
while not youtube_api_key.isalnum():
    youtube_api_key = raw_input('Enter your YouTube API Key: ')
    # Did you press enter?
    if not youtube_api_key:
        # Stop the program execution. Bye-Bye!
        exit(0)

# Search for Coding 101 videos using the channel ID and our API key
youtube_response = urllib2.urlopen(
    'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCSxIcr2rZZcoU7rSGXaEQag&maxResults=20&order=date&key=' + youtube_api_key)

# Load the list of videos returned by YouTube
videos = json.load(youtube_response)

# Declare the episodes list
episodes = []

# Loop through the videos to fill in the episodes list
for video in videos['items']:
    # Ensure that it is a video
    if video['id']['kind'] == 'youtube#video':
        # Store the title, description and link of the video in our list, separated by tabs
        # The format is: Title<TAB>Description<TAB>URL
        episodes.append(
            video['snippet']['title'] + '\t' + video['snippet']['description'] + '\t'
            + 'http://youtube.com/watch?v=' + video['id']['videoId'])

# Reverse sort the episodes list
episodes.reverse()

# Let's go. The program will execute until run = False
run = True
while run:
    print
    print 'Choose an episode:'
    print

    # Loop through and print the episodes list.
    count = 0
    for episode in episodes:
        # Split the episode info using tab as the delimiter
        episode_info = episode.split('\t')
        # Print the loop count & title
        # The count is converted into a str, and right justified
        print '  {0}. {1}'.format(str(count).rjust(2), episode_info[0])
        # Increment the loop count, unless we're on the last episode
        if (count + 1) < len(episodes):
            # Same as: count = count + 1
            count += 1

    print

    # Ask for the episode number
    choice = raw_input('Enter 0-' + str(count) + ' (or ENTER to quit): ')

    # Did you press enter?
    if not choice:
        # Stop the program execution. Bye-Bye!
        run = False

    # Validate the selected episode number. It must be a number...
    elif choice.isdigit():
        # Convert the selection to an integer
        selection = int(choice)

        # It must also be between 0 and the total number of episodes
        # Could be written as: selection >= 0 and selection <= count
        if 0 <= selection <= count:
            print
            print
            print '=============================================================================='
            # Split the selected episode info using tab as the delimiter
            episode_info = episodes[selection].split('\t')
            # Print the episode title
            print episode_info[0]
            print
            # Print the description, using textwrap to make it look pretty
            print textwrap.fill(episode_info[1], width=76)
            print
            # Print the URL
            print episode_info[2]
            print '=============================================================================='
            print
            raw_input('Press ENTER to continue...')