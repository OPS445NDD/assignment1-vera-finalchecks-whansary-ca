#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Walid Hasan Ansary"
Semester: "Summer 2026"

The python code in this file (assignment1.py) is original work written by
"Walid Hasan Ansary". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    mon_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if month == 2 and leap_year(year):
        return 29
    return mon_dict[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    
    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    if len(date) != 10:
        return False
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        return False
        
    if month < 1 or month > 12:
        return False
    if day < 1 or day > mon_max(month, year):
        return False
        
    return True

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    weekend_count = 0
    current_date = start_date
    
    while True:
        y, m, d = [int(x) for x in current_date.split('-')]
        day_str = day_of_week(y, m, d)
        
        if day_str in ['sat', 'sun']:
            weekend_count += 1
            
        if current_date == stop_date:
            break
            
        current_date = after(current_date)
        
    return weekend_count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        
    date1 = sys.argv[1]
    date2 = sys.argv[2]
    
    if not valid_date(date1) or not valid_date(date2):
        usage()
        
    if date1 < date2:
        start_date = date1
        stop_date = date2
    else:
        start_date = date2
        stop_date = date1
        
    weekends = day_count(start_date, stop_date)
    print(f"The period between {start_date} and {stop_date} includes {weekends} weekend days.")
