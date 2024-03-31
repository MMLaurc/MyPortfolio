# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"
REPORT_LJUST = 45

def reg_user():
    '''Add a new user to the user.txt file'''

    # - Request input of a new username
    new_username = input("New Username: ")

    # - Check if user already exists
    if new_username in username_password.keys():
        print("User already exists")
        return

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    
    # - Get the list of tasks for the current user
    current_user_task_list = [t for t in task_list if t['username'] == curr_user]
    
    # - Check if user has any tasks
    if len(current_user_task_list) < 1:
        print("Your don't have any tasks")
        return

    # - Display the tasks
    for i, t in enumerate(current_user_task_list):
        disp_str  = f"Task ID: \t {i + 1}\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

    while True:
        try:
            task_id = int(input("Enter a Task ID (type -1 to exit): "))
        except:
            print("Task ID must be a number")
            continue
        
        # - Exit the task menu if user types in -1
        if task_id == -1:
            break

        # - Check if there is a task with that id
        if task_id <= 0 or task_id > len(current_user_task_list):
            print("Task ID was not recognized")
            continue
        
        # - Task IDs are shown in a user friendly counting (+1), revert it to index style counting
        task_id -= 1

        task_menu = input('''Select one of the following Options below:
c - Mark task as complete
e - Edit task
: ''').lower()
        
        if task_menu == 'c':
            current_user_task_list[task_id]['completed'] = True
            write_tasks_to_file()
        
        elif task_menu == 'e':
            edit_task(current_user_task_list[task_id])

        else:
            print("You have made a wrong choice, Please Try again")

def edit_task(task):
    if task['completed'] == True:
        print("You cannot edit a completed task, Please Try another task")
    else:
        while True:
            task_editing_menu = input('''Select one of the following Options below:
a - Change the asigned person
d - Change the due date
: ''').lower()
                    
            if task_editing_menu == 'a':
                while True:
                    new_asignee = input("Type in the new asignee: ")

                    if new_asignee not in username_password.keys():
                        print("There is no user with this name, Please try again")
                        continue
                    
                    task['username'] = new_asignee
                    task['assigned_date'] = datetime.now()
                    write_tasks_to_file()
                    break
                break

            elif task_editing_menu == 'd':
                while True:
                    try:
                        new_due_date = datetime.strptime(input("Type in the new due date (YYYY-MM-DD): "), DATETIME_STRING_FORMAT)
                    except:
                        print("New Due Date is not in the correct format, Please try again")
                        continue
                    
                    task['due_date'] = new_due_date
                    write_tasks_to_file()
                    break
                break
            
            else:
                print("You have made a wrong choice, Please Try again")

def write_tasks_to_file():
    with open("tasks.txt", "w") as out_file:
        tasks_to_write = []
        for t in task_list:
            tasks_to_write.append(f"{t['username']};{t['title']};{t['description']};{t['due_date'].strftime(DATETIME_STRING_FORMAT)};{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)};{'Yes' if t['completed'] == True else 'No'}")
        out_file.write("\n".join(tasks_to_write))

def generate_reports():
    # - Generate tasks overview file
    with open("task_overview.txt", "w") as out_file:
        completed_tasks = [t for t in task_list if t['completed'] == True]
        incomplete_tasks = [t for t in task_list if t['completed'] != True]
        overdue_tasks = [t for t in incomplete_tasks if t['due_date'] < datetime.now()]

        out_file.write("-----------------------------------\n")
        out_file.write(f"Number of tasks: ".ljust(REPORT_LJUST) + f"{len(task_list)}\n")
        out_file.write(f"Completed tasks: ".ljust(REPORT_LJUST) + f"{len(completed_tasks)}\n")
        out_file.write(f"Incompleted tasks: ".ljust(REPORT_LJUST) + f"{len(incomplete_tasks)}\n")
        out_file.write(f"Overdue tasks: ".ljust(REPORT_LJUST) + f"{len(overdue_tasks)}\n")
        out_file.write(f"Percentage of incomplete tasks: ".ljust(REPORT_LJUST) + f"{percentage(len(incomplete_tasks), len(task_list))}%\n")
        out_file.write(f"Percentage of overdue tasks: ".ljust(REPORT_LJUST) + f"{percentage(len(overdue_tasks), len(task_list))}%\n")
        out_file.write("-----------------------------------")   

    # - Generate users overview file
    with open("user_overview.txt", "w") as out_file:
        out_file.write("-----------------------------------\n")
        out_file.write(f"Number of users: \t {len(username_password.keys())}\n")
        out_file.write(f"Number of tasks: \t {len(task_list)}\n")

        for username in username_password.keys():
            assigned_tasks = [t for t in task_list if t['username'] == username]
            completed_tasks = [t for t in assigned_tasks if t['completed'] == True]
            incomplete_tasks = [t for t in assigned_tasks if t['completed'] != True]
            overdue_tasks = [t for t in incomplete_tasks if t['due_date'] < datetime.now()]

            out_file.write("\n" + f" {username} ".center(35, '*') + "\n")
            out_file.write(f"Assigned tasks: ".ljust(REPORT_LJUST) + f"{len(assigned_tasks)}\n")
            out_file.write(f"Percentage of assigned tasks out of all: ".ljust(REPORT_LJUST) + f"{percentage(len(assigned_tasks), len(task_list))}%\n")
            out_file.write(f"Percentage of completed assigned tasks: ".ljust(REPORT_LJUST) + f"{percentage(len(completed_tasks), len(assigned_tasks))}%\n")
            out_file.write(f"Percentage of incomplete assigned tasks: ".ljust(REPORT_LJUST) + f"{percentage(len(incomplete_tasks), len(assigned_tasks))}%\n")
            out_file.write(f"Percentage of overdue tasks: ".ljust(REPORT_LJUST) + f"{percentage(len(overdue_tasks), len(assigned_tasks))}%\n")
            out_file.write("***********************************\n")

        out_file.write("-----------------------------------") 

    print("Reports were successfully generated")

def display_reports():
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()

    print("Tasks Overview:\n")
    with open("task_overview.txt", 'r') as task_overview_file:
        for line in task_overview_file.readlines():
            print(line)

    print("\nUsers Overview:\n")
    with open("user_overview.txt", 'r') as user_overview_file:
        for line in user_overview_file.readlines():
            print(line)

def percentage(part, whole):
    if whole == 0:
        return 0
    
    return 100 * float(part) / float(whole)

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr' and curr_user == 'admin':
        '''If the user is an admin they can generate reports about number of users
            and tasks.'''
        generate_reports()
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        display_reports()   

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")