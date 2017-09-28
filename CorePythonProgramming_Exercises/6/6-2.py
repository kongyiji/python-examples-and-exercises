#!/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to the Identifier Checker v1.0')
# print('Testees must be at least 2 chars long.')
print('Testees must be at least 1 chars long.')
# myInput = raw_input('Identifier to test? ')
myInput = input('Identifier to test? ')

if len(myInput) >= 1:

    if myInput[0] not in alphas:
        print('''invalid: first symbol must be alphabetic''')
    elif myInput in keyword.kwlist:
        print('''It's a Python Keyword''')
    else:
        for otherChar in myInput[1:]:
            alphnums = alphas + nums
            if otherChar not in alphnums:
                print('''invalid: remaining
                    symbols must be alphanumeric''')
                break
        else:
            print("okay as an identifier")