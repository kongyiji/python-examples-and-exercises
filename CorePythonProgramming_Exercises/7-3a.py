#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

d = {'a': 'hello', 'c': '!', 'b': 'world'}

print('Dictionary is', d)
print('Before sorted:', d.keys())

after_d = sorted(d.keys())

print('After sorted:', after_d)