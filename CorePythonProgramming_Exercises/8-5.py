#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def getfactors(num):
    factors = [num]
    count = num // 2
    while count > 1:
        if num % count == 0:
            factors.append(count)
        count -= 1
    factors.append(1)

    return factors

if __name__ == '__main__':
    result = getfactors(50)
    print(result)