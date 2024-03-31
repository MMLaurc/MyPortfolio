print("The working time start at 08:00 and end at 16:00.")
what_time = int(input("Please enter the time when you want to enter at work:"))

#this is an example of logical error because those if statement are not in right order       
  
if what_time in range(8, 16):
    print("You are on working time right now, go back at work!")
    
elif what_time == 16:
    print("Your job end now, you can go home and relax!")
    
elif what_time == 8:
    print("Your job start right now, prepeare for a productive day")
    
else:
    print("Out of working time, plese go home and relax for next day!")    



# This is the right order to function the program
# if what_time == 8:
#     print("Your job start right now, prepeare for a productive day")
       
# elif what_time == 16:
#     print("Your job end now, you can go home and relax!")
  
# elif what_time in range(8, 16):
#     print("You are on working time right now, go back at work!")
    
# else:
#     print("Out of working time, plese go home and relax for next day!")    