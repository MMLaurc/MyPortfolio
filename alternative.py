#create sentence
string = "Today I will try to understand more about strings "
new_string = ""

#create a for loop to change one letter upper and one lower
for i in range(len(string)):
    if i % 2 == 1:
        new_string += string[i].lower()
    else:
        new_string += string[i].upper()
print(new_string)       

string_list = string.split()

#create a for loop to change one word upper and one lower
for i in range(len(string_list)):
    if i % 2 == 1:
        string_list[i] = string_list[i].lower()                 
    else:
        string_list[i] = string_list[i].upper()
print(" ".join(string_list))



