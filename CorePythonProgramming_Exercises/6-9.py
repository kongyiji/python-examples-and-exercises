#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def convert_to_hour_and_minute(m):
    hour = m // 60
    minute = m % 60
    return hour, minute

def main():
    t_string = input('Please input time(minutes):')
    h, m = convert_to_hour_and_minute(int(t_string))
    print('%s convert to hours and minutes is: %s:%s' %(t_string, h, m))

if __name__ == '__main__':
    main()