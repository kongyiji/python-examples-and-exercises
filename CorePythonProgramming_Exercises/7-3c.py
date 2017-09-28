#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

d = {1: 'a', 2: 'c', 3: 'b'}

print('Dictionary is', d)

print('After sorted:')
for value in sorted(d.values()):
    for key in d.keys():
        if value == d[key]:
            print(key, ':', value)