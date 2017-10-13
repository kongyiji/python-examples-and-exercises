#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

a = {
    1 : 'first',
    2 : 'second',
    3 : 'third',
    4 : 'forth'
}

print('before:', a)

list_ak = list(a.keys())
list_av = list(a.values())

rev_a = dict(zip(list_av, list_ak))
print('after:', rev_a)