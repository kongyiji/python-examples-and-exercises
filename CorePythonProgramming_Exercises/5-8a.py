#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def square_area(l):
    '计算正方形面积'
    return l * l

def cube_area(l):
    '计算立方体面积'
    return 3 * l * l

def cube_volume(l):
    '计算立方体体积'
    return l * l * l

def main():
    i = input('请输入边长： ')
    l = int(i)

    sa = square_area(l)
    ca = cube_area(l)
    cv = cube_volume(l)

    print('正方形面积是：', sa)
    print('立方体面积是：', ca)
    print('立方体体积是：', cv)

if __name__ == '__main__':
    main()