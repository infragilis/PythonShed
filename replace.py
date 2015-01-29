#!/usr/bin/python
# boonstra 2014

import os
import sys
import fileinput

print ("Text to search for:")
textToSearch = raw_input( "> " ) 

print ("Text to replace it with:")
textToReplace = raw_input( "> " )

print ("File to perform Search-Replace on:")
fileToSearch  = raw_input( "> " )
#fileToSearch = 'D:\dummy1.txt'

tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('Match Found')
    else:
        print('Match Not Found!!')
    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()


raw_input( '\n\n Press Enter to exit...' )

