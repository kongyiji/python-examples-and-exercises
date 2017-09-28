#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

s = input('Please input a string: ')
l = len(s)
i = 0

print( 'use while loop to show character: ' )
while i < l:
    if i == 0:
        print('first character: ',s[0], s[1])
    elif i == (l-1):
        print('last character: ',s[l-2], s[l-1])
    else:
        print(s[i-1], s[i], s[i+1])
    i += 1

print( 'use for loop to show character: ' )
for i in range(l):
    if i == 0:
        print('first character: ',s[0], s[1])
    elif i == (l-1):
        print('last character: ',s[l-2], s[l-1])
    else:
        print(s[i-1], s[i], s[i+1])