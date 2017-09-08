#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from math import pi

def circle_area(r):
    '计算圆的面积'
    return pi * r * r

def orb_area(r):
    '计算球体的面积'
    return 4 * pi * r * r

def orb_volume(r):
    '计算球体的体积'
    return 4 * pi * r * r * r / 3

def main():
    r = float(input('请输入半径：'))

    ca = circle_area(r)
    oa = orb_area(r)
    ov = orb_volume(r)

    print('圆的面积是：', ca)
    print('球体的面积是：', oa)
    print('球体的体积是：', ov)

if __name__ == '__main__':
    main()