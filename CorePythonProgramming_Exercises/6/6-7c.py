#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python2

# 输入数字
num_str = raw_input('Enter a number: ')

# 转换成int类型
num_num = int(num_str)

# 生成从1开始到输入数字为止的序列
fac_list = range(1, num_num+1)
print "BEFORE:", fac_list

# 设置i的初始值
i = 0

# 循环条件
while i < len(fac_list):

    # 删除能整除的数
    if num_num % fac_list[i] == 0:
        del fac_list[i]

    # 不能整除时才递增
    else:
        # 递增
        i = i + 1

# 输出结果
print "AFTER", fac_list