#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

str = input('Please input string: ')

l = len(str)

if l % 2 == 0:
    half_l = int(l/2)
    for i in range(half_l):
        if str[i] != str[half_l + i]:
            print('Not Repeat!!!')
            break

    else:
        print('Repeat!!!')

else:
    print('Not Repeat!!!')