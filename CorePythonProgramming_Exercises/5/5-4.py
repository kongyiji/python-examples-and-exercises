#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def is_leap_year(year):

    remainder = year % 4

    if remainder == 0:
        if year % 100 != 0:
            print('%s is a leap year.' % (year))
        else:
            if year % 400 == 0:
                print('%s is a leap year.' % (year))
            else:
                print('%s is not a leap year.' % (year))
    else:
        print('%s is not a leap year.' % (year))

def main():
    year = int(input('Please input the year: '))
    is_leap_year(year)

if __name__ == '__main__':
    main()