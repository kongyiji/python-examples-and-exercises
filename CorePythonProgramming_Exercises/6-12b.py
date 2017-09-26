#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def rfindchr(string, char):

    string_length = int(len(string))
    rstring = string[::-1]
    for i in range(string_length):
        if rstring[i] == char:
            return string_length - i - 1
    else:
        return -1

if __name__ == '__main__':

    str = input('Please input string:\n')
    ch = input('Please input character to search(show last one):\n')
    ind = rfindchr(str, ch)
    print(ind)