#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from math import pow

drate = input('Please input day rate(%):')

yrate = pow((1+float(drate)), 365)

print('Year rate is:', yrate, '%')
