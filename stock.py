#!/usr/bin/env python

from time import ctime
from urllib import urlopen

tick = ('YHOO', 'GOOG', 'EBAY', 'AMZN')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=&f=sllclp2'

print '\nPrices quoted as of:', ctime()
print '\nTICKER'.ljust(9), 'PRICE'.ljust(8), 'CHG'.ljust(5), '%AGE'
print '------'.ljust(8), '-----'.ljust(8), '---'.ljust(5), '----'
u = urlopen(URL % ','.join(ticks))

for row in u:
    tick, price, chg, per = row.split(',')
    print eval(tick).ljust(7), \
            ('%.2f' % round(float(price), 2)).rjust(6), \
            chg.rjust(6), eval(per.rstrip()).rjust(6)

f.close()
