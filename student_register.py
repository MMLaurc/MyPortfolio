# create a variable to take number of students for exam and add exception
# in case they will add something else than numbers




while True:
    try:
        val = int(input("Please enter how many students will be register for exam! : "))
    except ValueError:
        print("This is not a number, please insert a valid number!")
        continue
    else:
        print(f"{val} students will participate at exam!")
        break
    
    
# open document reg_form.txt and write inside with a loop students id's
with open("reg_form.txt", "w+", encoding='utf-8') as id_student:
    id_student.writelines(f"There are {val} students registered!\n")
    id_student.writelines("Student ID and Signature: \n")
    for reg in range(val):
        user_input = (input("Please enter student ID number: "))
        id_student.write(f"Student ID : {user_input}................... \n")

