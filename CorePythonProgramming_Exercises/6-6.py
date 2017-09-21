#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

str = input('Please input a string: ')
i = 0
l = len(str)

while True:
    if str[i] == ' ':
        i += 1
    else:
        break

while True:
    if str[l-1] == ' ':
        l -= 1
    else:
        break

new_str = str[i:l]
print('New string is:')
print(new_str)