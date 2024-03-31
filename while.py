"""
 create 3 variable one to store data from user, and two for calculation
 create while loop to request input from user
 if imput from user is -1 brake the request and calculate the average   
 add condition if counter is bigger than 0 to print 0 otherwise will be error
 no division to 0
"""

request_number = 0
total = 0
counter = 0
 
while request_number != -1:
    request_number = int(input("Please enter a number:"))
    if request_number != -1:
        total += request_number
        counter += 1

if counter > 0:
        print(total/counter)   
else:
    print(0)

    


