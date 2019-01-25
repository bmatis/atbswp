#!/usr/bin/env python3
# selectiveCopy.py - walks through folder tree and searches for files
# with a certain extension and copies only those to a new location

import os, shutil

def selectiveCopy(folder, extension, destination):
    """
    Finds and copies all files in a folder with the given extension
    to a new location.
    """
    folder = os.path.abspath(folder)

    # check if destination exists and if not, create it
    if not os.path.exists(destination):
        print('Destination does not exist, creating %s...' % (destination))
        os.makedirs(destination)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                print("Copying: %s..." % (filename))
                sourceFile = os.path.join(foldername, filename)
                shutil.copy(sourceFile, destination)

selectiveCopy('.', '.py', '/Users/bmatis/copied_2')