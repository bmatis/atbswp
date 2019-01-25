#!/usr/bin/env python3
# urlFinder.py - Finds url addresses on the clipboard.

import pyperclip, re

# URL regex
# urlRegex = re.compile(r'''(
#     http
#     s?
#     ://
#     .*
#     [a-zA-Z0-9/]$
#     )''', re.VERBOSE)

urlRegex = re.compile(r'(https?://[^<>\s\'",]+)')

# find matches in clipboard text
text = str(pyperclip.paste())
matches = []
print(urlRegex.findall(text))
for groups in urlRegex.findall(text):
    matches.append(groups)

# Copy results to clipboard
if len(matches) > 0:
    #results = '\n'.join(matches)
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No URL addresses found.')
