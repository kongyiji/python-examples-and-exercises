#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def sortTwoNum_LargeToSmall(m, n):
    if m < n:
        m, n = n, m
    return m, n

def sortThreeNum_LargeToSmall(x, y, z):
    x, y = sortTwoNum_LargeToSmall(x, y)
    x, z = sortTwoNum_LargeToSmall(x, z)
    y, z = sortTwoNum_LargeToSmall(y, z)
    return x, y, z

def main():
    # User input
    print('Please input three numbers: ')
    a = input('Input first number: ')
    b = input('Input second number: ')
    c = input('Input third number: ')
    print('Before sorted: %s, %s, %s: ' %(a, b, c))

    # Sort
    a, b, c = sortThreeNum_LargeToSmall(int(a), int(b), int(c))

    # Output
    print('After sorted: %s, %s, %s: ' %(a, b, c))

if __name__ == '__main__':
    main()