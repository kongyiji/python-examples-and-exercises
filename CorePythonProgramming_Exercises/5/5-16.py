#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

origin_balance = float(input('Enter opening balance: '))
payment = float(input('Enter monthly payment: '))

title = '''
     Amount Remaining
Pymt#    Paid     Balance
-----    ------   ---------
'''

i = 0
rest_balance = origin_balance
print(title)
print('%-9d$%-8.2f$%-8.2f' %(i, 0, rest_balance))

while True:
    if payment < rest_balance:
        i += 1
        rest_balance -= payment
        print('%-9d$%-8.2f$%-8.2f' % (i, payment, rest_balance))
    else:
        i += 1
        print('%-9d$%-8.2f$%-8.2f' % (i, rest_balance, 0))
        break
