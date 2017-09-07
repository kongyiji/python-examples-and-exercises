#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def greatest_common_divisor(a, b):

    if (a == 0) and (b == 0):
        print('not exist greatest common divisor')
        exit(1)

    elif a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a

def least_common_multiple(a, b):

    if (a == 0) or (b == 0):
        print('least common multiple is 0')
        exit(0)

    if a > b:
        temp = a
    else:
        temp = b

    while True:
        if (temp % a == 0) and (temp % b == 0):
            return temp
        temp += 1

def main():

    print('Please input two interger number:')
    a = int(input('first number: '))
    b = int(input('second number: '))

    if a < 0 or b < 0:
        print('negative number is invalid.')

    r1 = greatest_common_divisor(a, b)
    r2 = least_common_multiple(a, b)

    print('%s and %s greatest common divisor is %s' %(a, b, r1))
    print('%s and %s least common multiple is %s' %(a, b, r2))

if __name__ == '__main__':
    main()