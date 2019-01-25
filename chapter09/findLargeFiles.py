#!/usr/bin/env python3
# findLargeFiles.py - walks through a folder tree and searches for files
# that are over a given size. Lists them and their size.

import os

def findLargeFiles(folder, size):
    """
    Finds and lists all files within a given directory that are over the
    given size.
    """
    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # determine if file is larger than given size
            file = os.path.join(foldername, filename)
            fileSize = os.path.getsize(file)
            if fileSize >= size:
                print(filename + ": " + str(fileSize))

findLargeFiles('.', 10000)