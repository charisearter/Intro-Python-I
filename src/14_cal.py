"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# Person inputs year and month
# if not specified do current month and year (no arguments)
# if one argument is specified assuming month) print for that month and year (1 argument 1 -12)
# if 2 arguments (month and year) use users month and year ( month year)
# Print usage statment showing expected arguments with brackets
# to get arguments use sys.argv -> get the length
# 1st argument is name of file argv[0]
# 2nd argument is month 00 - 12 argv[1]
# 3rd argument is year argv[2]
# (calender.textcalender has method that lets you format the dates)
# if argv length is 1 that means no arguments inputed give current month and year (file name is always [0])
# if argv length is 2 , argv[1] = should be 1 thru 12 and is the month --> do that month and current year
# if argv length is 3, argv[2] = year 4 digits --> do the month and year user inputted

x = datetime.now()

if(len(sys.argv) == 1):
    calendar.prmonth(x.year, x.month)
elif(len(sys.argv) == 2):
    calendar.prmonth(x.year, int(sys.argv[1]))
elif(len(sys.argv) == 3):
    calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
    print('Enter the month and year as m/yyyy')
