#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

'''
参考
http://blog.csdn.net/qq_35664993/article/details/53157561
'''

def convert_int(b):
    # 转换为4个段的列表
    b_list = b.split('.',4)
    # a_list.reverse()
    b_str = ''
    for i in b_list:
        b_str += bin(int(i))[2:].rjust(8, '0') # 字符串

    # print a_str
    return int(b_str,2)

if __name__ == '__main__':
    b = input('您需要将IP转为整型，请输入IP：\n')
    result = convert_int(b)
    print(result)