#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def check_divide(a, b):

    if a % b == 0:
        print('%d能被%d整除' %(a, b))
        return True
    else:
        print('%d不能被%d整除' % (a, b))
        return False

def main():

    print('请输入两个整数：')
    x = int(input('请输入第一个整数：'))
    y = int(input('请输入第二个整数：'))

    if x >= y:
        check_divide(x, y)
    else:
        check_divide(y, x)

if __name__ == '__main__':
    main()