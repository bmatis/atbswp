#!/usr/bin/env python3

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# value = '415-555-1234'
# print(value + ' is a phone number')
# print(isPhoneNumber(value))
# value = 'Moshi moshi'
# print(value + ' is a phone number')
# print(isPhoneNumber(value))

message = 'Call me at 805-555-1234 tomorrow. 805-555-4321 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
