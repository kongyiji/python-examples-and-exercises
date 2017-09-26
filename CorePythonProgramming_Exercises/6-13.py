#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

'''
来源
http://blog.csdn.net/zflzfl1023/article/details/38360257
'''

def atoc(compl_string):
    if compl_string[-1] not in 'jJ':
        compl_real = float(compl_string)
        compl_imag = 0.0
    else:
        for x in range(len(compl_string) - 1, -1, -1):
            if (compl_string[x] in '+-') and (compl_string[x - 1] not in 'e' + 'E'):
                if x == 0:
                    compl_real = 0.0
                else:
                    compl_real = float(compl_string[:x])
                compl_imag = float(compl_string[x:len(compl_string) - 1])
    return complex(compl_real, compl_imag)


print(atoc('3e2-5.67e+3j'))