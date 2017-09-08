#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

import string

nums = string.digits

inputNumber = input('Please input numbers:')

if len(inputNumber) >= 1:

    for s in inputNumber[:]:
        if num not in nums:
            print('invalid: Please input only number.')
            break
