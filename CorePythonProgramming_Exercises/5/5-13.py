#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def convert_to_minute(h, m):
    return 60 * h + m

def main():
    t_string = input('Please input time(like HH:mm):')
    h, m = t_string.split(':')
    all_min = convert_to_minute(int(h), int(m))
    print('%s convert to minutes is: %s' %(t_string, all_min))

if __name__ == '__main__':
    main()