#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def plus(m, n):
    return m + n

def minus(m, n):
    return m - n

def product(m, n):
    return m * n

def division(m, n):
    return m / n

def mod(m, n):
    return m % n

def pow(m, n):
    return m ** n

def turn_int_or_float(number):
    try:
        return int(number)
    except ValueError:
        return float(number)

def operate(a, b, c):
    if b == '+':
        return plus(a, c)
    elif b == '-':
        return minus(a, c)
    elif b == '*':
        return product(a, c)
    elif b == '/':
        return division(a, c)
    elif b == '%':
        return mod(a, c)
    elif b == '**':
        return pow(a, c)
    else:
        print('invalid operation symbol, please retry.')
        exit()

def main():
    x, y, z = '', '', ''
    result_string = '%s = %s'
    expression = input('Please input the expression(like "number1 + number2"): ')

    try:
        x, y, z = expression.split()
    except (ValueError):
        print('invalid expression, please retry, notice the space')
        exit()

    x = turn_int_or_float(x)
    z = turn_int_or_float(z)

    result = operate(x, y, z)

    print(result_string %(expression, result))

if __name__ == '__main__':
    main()