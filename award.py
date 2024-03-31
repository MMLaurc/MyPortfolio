'''
I will create the main 3 events for triathlon
Swimming, Cycling and Running as a variable
I will set the value as integer to calculate the time
I will create variable total_time for events, after the value for all this 3 event is inserted
The total of how many minutes was done will be calculated
And the last I will create time range if that time is passed a diffrent award will be given
'''

#Triathlon events
swimming = int(input("Enter total time for swimming: "))
cycling = int(input("Enter total time for cycling: "))
running = int(input("Enter total time for running:"))


#Total time for events
total_time = int(swimming + cycling + running)
print(f"You finish triathlon in {total_time} minutes!")



#Time range
if total_time >= 111:
    print(f"Your time is {total_time} minutes that's mean you have ''No Award'' ")
elif total_time >= 110:
    print(f"Your time is {total_time} minutes that's mean you win ''Provincial Scrool'' ")
elif total_time >= 106:
    print(f"Your time is {total_time} minutes that's mean you win ''Provincial Scroll'' ")
elif total_time >= 105:
    print(f"Your time is {total_time} minutes that's mean you win ''Provincial Half Colours'' ")
elif total_time >= 101: 
    print(f"Your time is {total_time} minutes that's mean you win ''Provincial Half Colours'' ")
elif total_time <= 100:
    print(f"Your time is {total_time} minutes that's mean you win ''Provincial Colours'' ")
elif total_time >= 0:
    print(f"Your time is {total_time} minutes that's mean you win ''Provincial Colours'' ")    