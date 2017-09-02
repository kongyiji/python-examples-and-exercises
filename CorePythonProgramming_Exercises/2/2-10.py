#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

i = 0
while i not in range(1, 101):
    i = int(input('Please input a number between 1 and 100: '))

print('Input number is %s: ' % i)