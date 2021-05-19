# File: Project3.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 05/01/2021
# Date Last Modified: 05/01/2021
# Description of Program: building a Texas Covid cases data base.
import os.path

# Write a separate function that reads lines from the input file and creates two data structures: a dictionary and a list of county names.
def readline_helper(filename):
    # Assume for this function that the input file exists.
    # Read a line from the file; if it starts with '#' discard it. Otherwise, parse it into four fields: countyName, confirmedCases, probableCases, deaths.
    gaFile = open(filename, 'r')
    firstline = gaFile.readline()
    newdict = {}
    newlist = []
    sum_confirmed = 0
    sum_death = 0
    lines = gaFile.readlines()
    # Repeat the steps above for all lines in the file.
    for i in lines:
        if '#' in i:
            continue
        # Convert confirmedCases and deaths into integers; you may have to strip a newline from deaths, since it's at the end of the line.
        seline = i.strip().split(',')
        # Associate the pair (confirmedCases, deaths) with countyName in the dictionary.
        newdict[seline[0]] = (int(seline[1]), int(seline[3]))
        # Also keep a running list of county names.
        newlist.append(seline[0])
        # Keep a running total of confirmedCases and of deaths; you'll need those later.
        sum_confirmed += int(seline[1])
        sum_death += int(seline[3])
    # After you've processed all lines in the file, add one more record to the dictionary associating the total confirmed cases and total deaths with key 'Texas'.
    newdict['Texas']  = (sum_confirmed, sum_death)
    # close the file here
    gaFile.close()
    # Finally, return the pair (dictionary, list of county names).
    return newdict, newlist

# Now you'll build the query processing functionality. This will be your main function.
def main():
    # Check that the input file exists; if not, print the error message "File county-covid-data.txt" not found." and exit. You'll need to import os.path for this.
    filename = 'county-covid-data.txt'
    if not os.path.isfile(filename):
        print("File county-covid-data.txt not found.")
        return
    # From the input file, build your database (dictionary) and county list using the function described above.
    data = readline_helper(filename)
    # Print the welcome message.
    print('Welcome to the Texas Covid Database Dashboard.\nThis provides Covid data in Texas as of 1/26/21.\nCreating dictionary from file: county-covid-data.txt \n')
    print('Enter any of the following commands:\n'
          'Help  - list available commands;\n'
          'Quit - exit this dashboard;\n'
          'Counties - list all Texas counties;\n'
          'Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;\n'
          'Deaths <countyName>/Texas - Covid deaths in specified county or statewide.\n')
    # Accept commands from the user, parse them and process them. (Remember that case doesn't matter, but be sure to capitalize county names when using them as dictionary keys.)
    while True:
        command = input('\033[1mPlease enter a command: \033[0m')
        command.lower()
        # Given a Help command, print the Help message.
        if command == 'help':
            print('Help  - list available commands;\n'
          'Quit - exit this dashboard;\n'
          'Counties - list all Texas counties;\n'
          'Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;\n'
          'Deaths <countyName>/Texas - Covid deaths in specified county or statewide.\n')
        # Given a Quit command, say goodbye and exit.
        elif command == 'quit':
            print('Thank you for using the Texas Covid Database Dashboard.  Goodbye!')
            quit()
        # Given a Counties command, print the list of counties, 10 per line, from the list you've accumulated.
        elif command == 'counties':
            count = 0
            for i in range(len(data[1])):
                if count == 9:
                    print(data[1][i], end = ', \n')
                    count = 0
                else:
                    print(data[1][i], end = ', ')
                    count += 1
            print('\n')
        # Given a Cases command, if the input is 'Texas', get that info from the database. If a county, see if it's a Texas county and acceess the info from database. If not, print an error message. For this error you can use the county name as entered or in the .title() form.
        #  cases example: cases san SaBA
        elif command[0:5] == 'cases':
            if command[6:] == 'texas':
                print('Texas total confirmed Covid cases: {}'.format(data[0].get('Texas')[0]))
                print()
            elif (command[6:].title() in data[0]):
                print('{} county has {} confirmed Covid cases.'.format(command[6:].title(), data[0].get(command[6:].title())[0]))
                print()
            else:
                print('County {} is not recognized.'.format(command[6:].title()))
                print()
        # The Deaths command is handled similarly to the Cases command.
        # deaths example: deaths traVIS
        elif command[0:6] =='deaths':
            if command[7:] =='texas':
                print('Texas total confirmed Covid deaths: {}'.format(data[0].get('Texas')[1]))
                print()
            elif command[7:].title() in data[0]:
                print('{} county has {} fatalities.'.format(command[7:].title(),data[0].get(command[7:].title())[1]))
                print()
            else:
                print('County {} is not recognized.'.format(command[7:].title()))
                print()
        # Any other commands should be rejected.
        else:
            print('Command is not recognized.  Try again!')
            print()
main()




