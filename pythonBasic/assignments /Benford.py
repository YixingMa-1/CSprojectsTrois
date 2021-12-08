# File: Benford.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 04/21/2021
# Date Last Modified: 04/23/2021
# Description of Program: Testing Benford's Law by using census_2009 data

import os.path

def main():
    # Accept from the user the name of a file, containing the census data.
    # If no file of that name exists, print an error message and quit.
    filename = input('Enter the name of a file of census data: ')
    if not os.path.isfile(filename):
        print('File does not exist')
        return
    # Create an empty set to store unique population values.
    unique_val = set()
    # Create a dictionary for leading digit counts,
    leading_digit = {}
    # with entries of the form [digit:count]. Note that digit here is a character,
    # not a number. The counts should initially all be 0,
    # for the nine possible digits (no number will start with a '0').
    leading_digit['1'] = 0
    leading_digit['2'] = 0
    leading_digit['3'] = 0
    leading_digit['4'] = 0
    leading_digit['5'] = 0
    leading_digit['6'] = 0
    leading_digit['7'] = 0
    leading_digit['8'] = 0
    leading_digit['9'] = 0
    # Open the file. The first line in the file is a header. Ignore that one. For each of the remaining lines:
    infile = open(filename, 'r')
    text = infile.readlines()[1:]
    # Parse the line to extract the population number.
    # Add that to the set (it won't repeat if it's already there).
    # Get its first digit and increment the count for that digit in the dictionary.
    for line in text:
        line = line.strip()
        data = line.split()
        num = data[-1]
        unique_val.add(int(num))
        first_num = num[0]
        leading_digit[first_num] += 1
    # Close the file.
    infile.close()
    # Print to the terminal the line: "Output written to benford.txt"
    print('Output written to benford.txt')
    # Write the other output to a file named benford.txt: how many total population values;
    # how many unique population values; a table of results on the leading digits.
    # (See the examples below.) Note that each run of the program will overwrite the file.
    # (Hint: you may want to just print to the terminal until you get everything running, and then change to writing to a file.)
    total = len(text)

    newfile = open('benford.txt','w')
    newfile.write('Total number of cities: {}\n'.format(len(text)))
    newfile.write('Unique population counts: {}\n'.format(len(unique_val)))
    newfile.write('First digit frequency distributions:\n')
    newfile.write('Digit\tCount\tPercentage\n')
    for i in range(1, 10):
        count = leading_digit["{}".format(i)]
        perc = (100 * (count / total))
        formatted_freq = "{:.1f}".format(perc)
        newfile.write("{:<7d} {:<8d}{}\n".format(i, count, formatted_freq))

    newfile.close()


main()


