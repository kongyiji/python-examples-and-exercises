#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

i = float(input('Please input a number: '))

if i.isdigit():
    if i < 0:
        print('%f is a negative number.') % i
    elif i == 0:
        print('%f is zero.') % i
    else:
        print('%f is a positive number.') % i
