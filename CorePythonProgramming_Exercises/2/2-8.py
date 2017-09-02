#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

#t = (1, 2, 3, 4, 5)

t = []
print('Please input five numbers(use "," to split): ')
for a in range(5):
    tmp = input('%d: ' % (a + 1))
    t.append(int(tmp))


print( 'while loop result: ' )
i, r =0, 0
while i < len( t ):
    r = r + t[i]
    i += 1
print( 'Result is: %d' % r )

print( 'for loop result: ' )
i, r=0, 0
for i in range( len( t ) ):
    r = r + t[i]
    i += 1
print( 'Result is: %d' % r )
