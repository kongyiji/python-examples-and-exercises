#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from numpy import *

ma = array([[1, 2, 3], [4, 5, 6], [3, 6, 9]])
na = array([[9, 9, 9], [2, 4, 8], [5, 7, 1]])

m = mat(ma)
n = mat(na)

print('M:\n', m)
print('N:\n', n)

print('M + N =\n', m + n)
print('M * N =\n', m * n)