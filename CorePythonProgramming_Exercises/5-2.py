#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def product(m, n):
    return m * n

def main():
    print('Please input two numbers to product: ')
    a = input('first number: ')
    b = input('second number: ')
    result = product(float(a), float(b))
    print('%s product %s equals \n%s' %(a, b, result))

if __name__ == '__main__':
    main()