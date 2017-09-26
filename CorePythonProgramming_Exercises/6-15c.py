#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from datetime import *

def is_leap_year(year, count):

    remainder = year % 4

    if remainder == 0:
        if year % 100 != 0:
            count += 1
            # print('%s is a leap year.' % (year))
        else:
            if year % 400 == 0:
                count += 1
                # print('%s is a leap year.' % (year))
            # else:
                # print('%s is not a leap year.' % (year))
    # else:
        # print('%s is not a leap year.' % (year))
    return count

in_d = input('Please input birthday(like YYYY/MM/DD): ')
today = datetime.today()

d = datetime.strptime(in_d, '%Y/%m/%d')

if d > today:
    print("Wow!!! You come from future, aren't you?")
else:
    leap_count = 0
    for i in range(d.year, today.year):
        leap_count = is_leap_year(i, leap_count)

    birth_month = d.month
    birth_day = d.day
    next_birthday = datetime(today.year, birth_month, birth_day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birth_month, birth_day)

    next_birthday_days = (next_birthday - today).days
    delta_day = (today - d).days
    print('You borned', delta_day, 'days and', leap_count, 'leap year/years.')
    print('Next birthday will be', next_birthday_days, 'days later.')