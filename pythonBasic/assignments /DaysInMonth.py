# File: DaysInMonth.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 02/25/2021
# Date Last Modified: 02/26/2021
# Description of Program: Computing the numbers of days in a month

year = int(input('Please enter a year: '))
month = int(input('Please enter a month: '))

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if month % 2 == 1 and month <= 7:
    days = 31
elif month == 2:
    if leap_year(year) is True:
        days = 29
    else:
        days = 28
elif month % 2 == 0 and month <=7:
    days = 30
elif month % 2 == 1 and month > 7:
    days = 30
elif month % 2 == 0 and month > 7:
    days = 31

if month == 1:
    smonth = 'January'
elif month == 2:
    smonth = 'February'
elif month == 3:
    smonth = 'March'
elif month == 4:
    smonth = 'April'
elif month == 5:
    smonth = 'May'
elif month == 6:
    smonth = 'June'
elif month == 7:
    smonth = 'July'
elif month == 8:
    smonth = 'August'
elif month == 9:
    smonth = 'September'
elif month == 10:
    smonth = 'October'
elif month == 11:
    smonth = 'November'
elif month == 12:
    smonth = 'December'

print('{} {} has {} days'.format(smonth, year, days))




