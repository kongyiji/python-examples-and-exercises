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

def getprimefactors(num):
    factors = []
    count = num // 2
    while count > 1:
        if num % count == 0 and isprime(count):
            factors.append(count)
            num = num // count
            count = num
            continue
        count -= 1
    # factors.append(1)
    return factors

if __name__ == '__main__':

    num = 17
    primefactors = []
    if isprime(num):
        primefactors.append(num)
    else:
        primefactors = getprimefactors(num)

    print(primefactors[::-1])