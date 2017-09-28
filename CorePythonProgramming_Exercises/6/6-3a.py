#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

import string

def large_to_small(a, b):
    if a < b:
        a, b = b, a
    return a, b

nums = string.digits

inputNumber = input('Please input several numbers, use space to split:')
numList = []

if len(inputNumber) >= 1:

    for i in inputNumber.split():
        try:
            int(i)
        except ValueError as e:
            print(e)

        numList.append(int(i))

    print(sorted(numList, reverse=True))