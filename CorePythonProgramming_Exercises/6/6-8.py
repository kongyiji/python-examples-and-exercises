#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def single_digit(i):
    'change single digit to english version'

    single_english = {
        0 : 'zero',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine'
    }

    return single_english[i]

def tens_digit(i):
    'change tens digit to english version'

    tens_english = {
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        2 : 'twenty',
        3 : 'thirty',
        4 : 'forty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety'
    }

    t = i // 10
    v = i % 10
    if t == 1:
        return tens_english[i]
    elif v == 0:
        return tens_english[t]
    else:
        return tens_english[t] + '-' + single_digit(v)

def hundreds_digit(i):
    'change hundreds digit to english version'

    t = i // 100
    v = i % 100
    str = single_digit(t) + ' hundred'

    if v != 0:
        str = str + ' and '
    else:
        return str

    if v // 10 != 0:
        str = str + tens_digit(v)
        return str
    else:
        str = str + single_digit(v)
        return str

def main():

    i = input('Please input a number between 0 and 1000: ')
    in_int = int(i)
    english_result = ''

    if in_int not in range(0, 1001):
        print('Out of range.')
        exit(1)

    elif in_int // 1000 == 1:
        english_result = 'one thousand'

    elif in_int // 100 != 0:
        english_result = hundreds_digit(in_int)

    elif in_int // 10 != 0:
        english_result = tens_digit(in_int)

    else:
        english_result = single_digit(in_int)

    print(english_result)

if __name__ == '__main__':
    main()