#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

inputNumber = input('Please input several numbers, use space to split:')
numList = []

if len(inputNumber) >= 1:

    for i in inputNumber.split():
        try:
            int(i)
        except (ValueError, e):
            print(e)

        numList.append(int(i))

    print(sorted(numList, reverse=True))