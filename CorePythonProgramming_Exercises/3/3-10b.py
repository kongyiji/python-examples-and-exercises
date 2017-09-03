#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
import os

fname = input( 'Eneter filename: ' )
print()

# attempt to open file for reading
# try:
#     fobj = open( fname, 'r' )
# except IOError(e):
#     print( "*** file open error:", e )
if not os.path.exists(fname):
    print("ERROR: '%s' not exists" % fname)
else:
    # display contents to the screen
    fobj = open( fname, 'r' )
    for eachLine in fobj:
        print( eachLine, )
    fobj.close()
