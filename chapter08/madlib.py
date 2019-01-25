#!/usr/bin/env python3
# madlib.py - generates mad lib results
#
# Will check source file and look for any phrases in all caps. If phrase should
# be multiple words, seperate with underscores. These phrases are what will be
# replaced in the madlib and will be used to ask the user for input.
# examples: NOUN, ADJECTIVE, TYPE_OF_ANIMAL, PAST_TENSE_VERB

import re

def startsWithVowel(word):
    """
    Determine if given word starts with a vowel. Return True if it does
    and False if not.
    """
    vowelRegex = re.compile(r'(a|e|i|o|u)')
    firstLetter = word[0].lower()
    if vowelRegex.search(firstLetter):
        return True
    else:
        return False

file = open('madlib.txt', 'r')
madlib = file.read()
file.close()

# regex to look for text that is to be replaced.
madlibRegex = re.compile(r'[A-Z_]{3,}')

for text in madlibRegex.findall(madlib):
    # For purposes of nice looking display of the madlib text to the user,
    # convert it to lower case and convert any underscores to spaces.
    displayText = text.lower().replace('_', ' ')

    if startsWithVowel(text):
        # if the word starts with a vowel, use "an" in request
        replacement = input('Enter an %s: ' % displayText)
    else:
        # otherwise, use 'a' in request
        replacement = input('Enter a %s: ' % displayText)
    madlib = madlib.replace(text, replacement, 1)

print(madlib)

resultFile = open('madlib_result.txt', 'w')
resultFile.write(madlib)
resultFile.close()