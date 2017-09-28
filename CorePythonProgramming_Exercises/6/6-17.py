#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def myPop(l):

    print(l[-1])
    del l[-1]

if __name__ == '__main__':

    list = [1, 3, 5, 9]
    print('Before:', list)
    myPop(list)
    print('After:', list)