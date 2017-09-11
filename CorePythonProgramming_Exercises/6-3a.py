#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

import string

def large_to_small(a, b):
    if a < b:
        a, b = b, a
    return a, b

nums = string.digits

inputNumber = input('Please input numbers:')
lenInput = len(inputNumber)

if len(inputNumber) >= 1:

    numList = []

    for num in inputNumber[:]:
        if num not in nums:
            print('invalid: Please input only number.')
            break

        numList.append(num)

    for num in numList:
        print(num, end='')
    numList.sort()
    print()
    for num in numList:
        print(num, end='')