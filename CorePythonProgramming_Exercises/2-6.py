#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

p = input('Please input a number: ')
i = float(p)

if i < 0:
    print( '%d is a negative number.' % i)
elif i == 0:
    print( '%d is zero.' % i)
else:
    print( '%d is a positive number.' % i)
