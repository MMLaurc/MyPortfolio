"""
Create a variable as empty string for *
create a loop with a range of 1 to 10
add if <= to 5 because stars to be taken till 5
add else to start second part from last character
and print
"""

stars = ""

for i in range (1, 10):
    if i <= 5:
        stars += "*"
    else:
        stars = stars[:-1] 
                       
    print(stars)
    
        
    
    