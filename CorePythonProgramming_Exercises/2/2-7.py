#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

s = input('Please input a string: ')
l = len(s)
i = 0

print( 'use while loop to show character: ' )
while i < l:
    print(s[i])
    i += 1

print( 'use for loop to show character: ' )
for i in range(l):
    print(s[i])