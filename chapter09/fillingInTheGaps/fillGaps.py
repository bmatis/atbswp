#!/usr/bin/env python3
# fillGaps.py - finds files with given prefix in a folder. Finds gaps
# in the numbering and renames files to fill in the gaps.

import os, re, shutil

def addLeadingZeroes(number, desiredLength):
    numLeadingZeroes = desiredLength - len(str(number))
    return ('0' * numLeadingZeroes + str(number))

filenamePattern = re.compile(r"""
    ^(spam)         # prefix
    ((0)*(\d+))     # a number with leading zeroes
    (.txt)$         # file extension
    """, re.VERBOSE)

desiredNumber = 1

for filename in sorted(os.listdir('.')):
    mo = filenamePattern.search(filename)

    # Skip files that don't fit the pattern.
    if mo == None:
        continue

    # Get the different parts of the filename.
    prefix = mo.group(1)
    numWithLeadingZeroes = mo.group(2)
    number = mo.group(4)
    extension = mo.group(5)

    print("%s has the number: %s" % (filename, number))

    # check if number is next in sequence and if not, rename it to fill
    # the gap
    if int(number) != desiredNumber:
        number = desiredNumber
        number = addLeadingZeroes(number, 3)
        newFilename = prefix + str(number) + extension
        print("Renaming %s to %s" % (filename, newFilename))
        shutil.move(filename, newFilename)

    desiredNumber += 1