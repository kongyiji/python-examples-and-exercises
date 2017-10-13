#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

f = int(input('from:'))
t = int(input('to:')) + 1
i = int(input('increment:'))

for result in range(f, t, i):
    print(result)