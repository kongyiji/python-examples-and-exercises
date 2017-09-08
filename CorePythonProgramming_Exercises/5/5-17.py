#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from random import randint, choice



def new_random_list():
    'add random number to list'

    l = []
    N = randint(1, 100)
    for i in range(N):
        n = randint(0, (2 ** 31 - 1))
        l.append(n)
    # print(l)
    return l

def pickup_list(random_list):
    'pickup random items from old list to make new list'

    nl = []
    length = len(random_list)
    while True:
        N = randint(1, 100)
        if N <= length:
            break

    for i in range(N):
        nl.append(choice(random_list))

    # print(nl)
    return nl

def main():

    l1 = new_random_list()
    l2 = pickup_list(l1)
    l2.sort()
    print('随机生成的列表为：', l1)
    print('子集为', l2)

if __name__ == '__main__':
    main()