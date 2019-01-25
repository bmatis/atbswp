#! /usr/bin/env python3
# bulletPointAdder.py - Adds wikipedia bullet points to the start of each
# line of text on the clipboard.

import pyperclip

# Get the current content from the clipboard.
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Merge all the lines back into a single variable.
text = '\n'.join(lines)

# Put the modified results back into the clipboard.
pyperclip.copy(text)
