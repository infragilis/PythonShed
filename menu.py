#!/usr/bin/python
# infragilis 2015
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Generate random number"
    print "2. Ping a host"
    print "3. Replace a string within a doc"
    print "4. Logparser"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:    
        print "Menu 1 has been selected"
        execfile("Rgeneratev1.py")
    elif choice==2:
        print "Menu 2 has been selected"
        execfile("ping.py")
    elif choice==3:
        print "Menu 3 has been selected"
        execfile("replace.py")
    elif choice==4:
        print "Menu 4 has been selected"
        execfile("logparse.py")
    elif choice==5:
        print "Goodbye !"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
