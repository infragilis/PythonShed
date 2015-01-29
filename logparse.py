#!/usr/bin/python
# infragilis 2015, most platforms will require root access to logs
import platform
import sys
import mmap

print  "This is logparse v1 "

# Figure out where we are running on 
platformcheck = platform.platform()
print  "you are running on %s " % platformcheck
if "Darwin" in platformcheck:
    print "This is Darwin, default is /var/log/system.log"
elif "Ubuntu" in platformcheck:
    print "This is Ubuntu, default is /var/log/syslog"
elif "Redhat" in platformcheck:
        print "This is Redhat, default is /var/log/messages"
else: 
    print "Do not recognize platform...exiting"
    exit()   
#no need for regex, var is already doing that > error is ERROR is Error
errorvar = raw_input("What are you looking for:  ")   
print  "Parsing Logs ................ " 
# if Darwin ..
if "Darwin" in platformcheck:
        
        fh = open('/var/log/system.log')

        for line in fh:
            if errorvar in line:
                print line                              
# if Ubuntu ..

elif "Ubuntu" in platformcheck:
        
        fh = open('/var/log/syslog')

        for line in fh:
            if errorvar in line:
                print line                
# if Redhat ..
if "Redhat" in platformcheck:
        
        fh = open('/var/log/messages')

        for line in fh:
            if errorvar in line:
                print line
