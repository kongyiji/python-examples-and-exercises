#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def findchr(string, char):

    string_length = int(len(string))
    for i in range(string_length):
        if string[i] == char:
            return i
    else:
        return -1

if __name__ == '__main__':

    str = input('Please input string:\n')
    ch = input('Please input character to search(show first one):\n')
    ind = findchr(str, ch)
    print(ind)