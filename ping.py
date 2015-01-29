#!/usr/bin/python
#infragilis 2015
import os
user_input = raw_input("IP or name please:  ")  
print user_input

if os.system("ping -c 1 " + user_input ) == 0:
    print "host appears to be up"


