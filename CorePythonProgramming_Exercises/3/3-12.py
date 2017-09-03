#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

'''
You can choose
create text file
or
read and display text file
'''

import os

menu = '''
     Main Menu
--------------------
(C)reate text file
(D)isplay text file
(Q)uit
'''

def create_text_file():
    ls = os.linesep

    # get filename
    while True:

        fname = input( 'create a new file name: ' )
        if os.path.exists( fname ):
            print( "ERROR: '%s' already exists" % fname )
        else:
            break

    # get file content (text) lines
    all = []
    print( "\nEnter lines ('.' by itself to quit).\n" )

    # loop until user terminates input
    while True:
        entry = input( '>>> ' )
        if entry == '.':
            break
        else:
            all.append( entry )

    # write lines to file with proper line-ending
    fobj = open( fname, 'w' )
    fobj.writelines( ['%s%s' % (x, ls) for x in all] )
    fobj.close()
    print( 'DONE!' )

def display_text_file():
    fname = input( 'Eneter filename: ' )
    print()

    # attempt to open file for reading
    if not os.path.exists( fname ):
        print( "ERROR: '%s' not exists" % fname )
    else:
        # display contents to the screen
        fobj = open( fname, 'r' )
        for eachLine in fobj:
            print( eachLine.strip() )
        fobj.close()

def main():
    while True:
        choice = input(menu)
        if choice.lower() == 'c':
            create_text_file()
        elif choice.lower() == 'd':
            display_text_file()
        elif choice.lower() == 'q':
            print('quit normally')
            break
        else:
            print('invalid choice, please retry...')

if __name__ == '__main__':
    main()