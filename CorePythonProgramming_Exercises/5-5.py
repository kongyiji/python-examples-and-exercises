#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def change_money(money, cent):
    quoient, remainder = divmod(money, cent)
    return quoient, remainder

def main():

    money = int(input('请输入需要转换美分（小于1美元，1美元=100美分）: '))
    cent_coins = (25, 10, 5, 1)

    if money in range(1, 100):
        print('%s美分可以换成：' % (money))

        for cent_coin in cent_coins:
            q, r = change_money(money, cent_coin)
            if q != 0:
                print('%s枚%s美分的硬币' % (q, cent_coin))
            if r == 0:
                break
            else:
                money = r
                continue
    else:
        print('不合法的数值，请重新输入')

if __name__ == '__main__':
    main()