#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

menu = '''
    菜    单
------------------
(1) 取五个数的和
(2) 取五个数的平均数
(X) 退出
------------------
请选择三项中的一项
'''

def main():
    while True:
        choice = input( menu )
        if choice.isdigit() and int( choice ) == 1:
            print( '取和' )
        elif choice.isdigit() and int( choice ) == 2:
            print( '取平均值' )
        elif choice.lower() == 'x':
            print( '正常退出' )
            break
        else:
            print( '无效的选项，请重新输入' )

if __name__ == '__main__':
    main()