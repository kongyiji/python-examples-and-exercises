#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def subchr(string, origchar, newchar):

    # string_length = int(len(string))
    new_string = ''
    for s in string:
        if s == origchar:
            new_string += newchar
        else:
            new_string += s
    return new_string

if __name__ == '__main__':

    str = input('Please input string:\n')
    org_ch = input('Please input character to be replaced:\n')
    new_ch = input('Please input character to replace:\n')
    result = subchr(str, org_ch, new_ch)
    print(result)