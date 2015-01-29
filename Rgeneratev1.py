#!/usr/bin/python
# infragilis 2015
import random
import mmap

print "This is Rgenerate.py V1"
# Select random char A-Z and Select an even number 
char= random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
number= random.randrange(1000000000, 10000000000, 2,) 
print "%s%s" % (char, number)  #print both vars in one with formatting
user_input = raw_input("Some input please:  ")  #
#numbers only
if user_input.isalpha():
   print 'Two digits, numbers only please! the script will exit, please restart'
   exit()  #exit on letter
#no more than two   
elif len(user_input) > 2:
   print "Error! Only 2 digits allowed! the script will exit, please restart"
   exit()
#continue on numbers only       
if user_input.isdigit():  
   sum = float(number) + float(user_input) # add input to number
print "%s%s" % (char, int(sum)) # display the char and total without the decimels int()

varvalue= "%s%s" % (char, int(sum)) #dump both vars in one with formatting

#check if value exists in file before writing
f = open('values.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find(varvalue) != -1:
    print 'This value already exists the script will exit, please restart'
    exit()

#save the value to a file
f = open("values.txt",'a+') #opens file with name of "values.txt"
f.write(varvalue + '\n') #write var to file with newline
f.close() # close file

