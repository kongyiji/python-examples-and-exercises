#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from datetime import datetime, timedelta

in_d1 = input('Please input first date(like YYYY/MM/DD): ')
in_d2 = input('Please input second date(like YYYY/MM/DD): ')

d1 = datetime.strptime(in_d1, '%Y/%m/%d')
d2 = datetime.strptime(in_d2, '%Y/%m/%d')

if d1 < d2:
    d1, d2 = d2, d1

delta_day = (d1 - d2).days

print('days between two dates is ', delta_day, ' days')