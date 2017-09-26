#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

'''
参考
http://blog.csdn.net/qq_35664993/article/details/53157561
'''

def convert_ip(a):
    #先转换为二进制
    a_tem = bin(int(a))[2:]
    # 将所有的 0 补齐
    a_str = a_tem.rjust(32, '0')
    #切片处理
    a1 = a_str[0:8]
    a2 = a_str[8:16]
    a3 = a_str[16:24]
    a4 = a_str[24:]
    a_out= str(int(a1,2)) + '.' + str(int(a2 ,2)) + '.' + str(int(a3,2)) + '.' + str(int(a4,2))
    return a_out

if __name__ == '__main__':
    a = input('您需要将整型转为IP，请输入整型：\n')
    result = convert_ip(a)
    print(result)