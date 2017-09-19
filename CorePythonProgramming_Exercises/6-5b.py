#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

str1 = input('Please input first string: ')
str2 = input('Please input second string: ')

if len(str1) != len(str2):
    print('Not Match!!!')

else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print('Not Match!!!')
            break
    else:
        print('Match!!!')