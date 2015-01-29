#!/usr/bin/python
# infragilis 2015
import random


# Select random char A-Z and Select an even number 
char= random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
number= random.randrange(1000000000, 10000000000, 2,) 
print "%s%s" % (char, number)  #print both vars in one with formatting
user_input = raw_input("Some input please:  ")  #
sum = float(number) + float(user_input) # add input to number
print "%s%s" % (char, int(sum)) # display the char and total without the decimels int()

value= "%s%s" % (char, int(sum)) #dump both vars in one with formatting
f = open("values.txt",'a+') #opens file with name of "values.txt"
f.write(value + '\n') #write var to file with newline
f.close() # close file
