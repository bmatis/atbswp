#! /usr/bin/env python3

def printTable(table):
    """Take a list of strings and display it in a well-organized table."""
    colWidths = [0] * len(table)
    padding = 2

    for i in range(len(colWidths)):
        maxLength = len(max(table[i], key=len))
        colWidths[i] = maxLength + padding

    print()
    for item in range(len(table[0])):
        line = "|"
        for list in range(len(table)):
            line += table[list][item].rjust(colWidths[list])
            line += " |"
        print('-' * len(line))
        print(line)
    print('-' * len(line) + "\n")


tableData = [
                ['1', '2', '3', '4'],
                ['apples', 'oranges', 'red cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'elephants', 'goose'],
            ]

printTable(tableData)
