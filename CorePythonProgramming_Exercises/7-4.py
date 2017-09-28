#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

ks = [1, 2, 3, 4]
vs = ['abc', 'def', 'ghi', 'jkl']

new_dict = dict(zip(ks, vs))

print('two lists: %s %s' %(ks, vs))

print('new dictionary:', new_dict)