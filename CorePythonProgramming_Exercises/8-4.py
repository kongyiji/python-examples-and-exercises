#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def isprime(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True

for i in range(28, 50):
    r = isprime(i)
    print(i, r)