#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from string import ascii_lowercase, ascii_uppercase

def case_reversal(str):
    'change case write to reversal case'

    l = len(str)
    new_str = ''
    for i in range(l):
        if str[i] in ascii_uppercase:
            new_str += str[i].lower()
        elif str[i] in ascii_lowercase:
            new_str += str[i].upper()
        else:
            new_str += str[i]

    return new_str

def main():

    in_str = input('Please input a string: ')
    out_str = case_reversal(in_str)

    print("%s case reversal's result is %s" %(in_str, out_str))

    # another
    print("%s case reversal's result is %s" % (in_str, in_str.swapcase()))

if __name__ == '__main__':
    main()