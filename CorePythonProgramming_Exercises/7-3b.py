#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

d = {'a': 'hello', 'c': '!', 'b': 'world'}

print('Dictionary is', d)
# print('Before sorted:', d.keys())

print('After sorted:')
for d_key in sorted(d.keys()):
    print(d_key, ':', d[d_key])