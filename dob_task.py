#open the file DOB.text
with open("DOB.txt", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()
            
    #print string Name    
    print("\nName\n")  

    #Loop through file and take out names    
    for n in lines:
        names = n.strip()
        names = names.split()
        print(names[0],names[1])
        
    #Print string Date of Birth        
    print("\nDate of Birth: \n")
    
    #Loop thorugh file and take out date of births
    for d in lines:
        dob = d.strip()
        dob = dob.split()            
        print(dob[2],dob[3],dob[4])