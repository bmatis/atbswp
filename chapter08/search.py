#!/usr/bin/env python3
# search.py - searches all .txt files in a directory for any line that matches
# the user provided phrase. Prints the file and specific line to the screen.

import re, os

# Ask user for text to search for
print("What text would you like to find?")
searchText = input("> ")

print("\nOk, now searching for \"%s\"..." %searchText)

# regex for the search
searchRegex = re.compile(r'%s' %searchText, re.I)

# Function for finding the text in the file
def searchInFile(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    for line in lines:
        if searchRegex.search(line):
            print(fileName + ": " + line.rstrip())
    file.close()

# Loop for finding every .txt file in the directory
for fileName in os.listdir(os.getcwd()):
    if fileName[-4:] == '.txt':
        searchInFile(fileName)