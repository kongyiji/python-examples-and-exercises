#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def sortTwoNum_SmallToLarge(m, n):
    if m > n:
        m, n = n, m
    return m, n

def sortThreeNum_SmallToLarge(x, y, z):
    x, y = sortTwoNum_SmallToLarge(x, y)
    x, z = sortTwoNum_SmallToLarge(x, z)
    y, z = sortTwoNum_SmallToLarge(y, z)
    return x, y, z

def main():
    # User input
    print('Please input three numbers: ')
    a = input('Input first number: ')
    b = input('Input second number: ')
    c = input('Input third number: ')
    print('Before sorted: %s, %s, %s: ' %(a, b, c))

    # Sort
    a, b, c = sortThreeNum_SmallToLarge(int(a), int(b), int(c))

    # Output
    print('After sorted: %s, %s, %s: ' %(a, b, c))

if __name__ == '__main__':
    main()