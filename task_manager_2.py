def log_in():
    # This if statement only allows Admin to gain access to view all information. If a user
    # tries to open this file, an error message will appear and direct the user back to the
    # main menu or exit the program
    if username != "Admin":
        va_menu = input("\nYou are not permitted to view all tasks\n"
                        "\nSelect one of the following options:\n"
                        "Enter '-1' to return to the main menu\n"
                        "Enter 'e' to exit\n")

        if va_menu == "-1":
            user_main_menu()

        elif va_menu != "e":
            va_menu = input("\nYou have entered an invalid option\n"
                            "\nSelect one of the following options:\n"
                            "Enter '-1' to return to the main menu\n"
                            "Enter 'e' to exit\n")

            # The user will be directed back to the main menu with the 'main_menu()' function
            if va_menu == "-1":
                user_main_menu()

        else:
            print("Login terminated")


def admin_main_menu():
    if username == "Admin":

        print("""
        Please select one of the following options:\n
        r - register new user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate report
        ds - display statistics
        e - exit\n""")

        choice_a = input("")

        # The if statement will check the conditions for 'r - register new user'
        if choice_a == "r":
            reg_user()

        # The elif statement will check the conditions for 'a - add task'
        elif choice_a == "a":
            add_task()

        # The elif statement will check the conditions for 'va - view all tasks'
        elif choice_a == "va":
            view_all()

        # The elif statement will check the conditions for 'vm - view my tasks'
        elif choice_a == "vm":
            view_mine()

        # The elif statement will check the conditions for 'gr - generate reports'
        elif choice_a == "gr":
            gen_report()

        # The elif statement will check the conditions for 'ds - display statistics'
        elif choice_a == "ds":
            display_stats()

        if choice_a == "e":
            print("Session ended")


def user_main_menu():
    if username != "Admin":

        print("""
            Please select one of the following options:\n
            r - register new user
            a - add task
            vm - view my tasks
            e - exit\n""")

        choice_u = input("")

        # The if statement will check the conditions for 'r - register new user'
        if choice_u == "r":
            reg_user()

        # The elif statement will check the conditions for 'a - add task'
        elif choice_u == "a":
            add_task()

        # The elif statement will check the conditions for 'vm - view my tasks'
        elif choice_u == "vm":
            view_mine()

        if choice_u == "e":
            print("Session ended")


def reg_user():

    # If the username is equal to 'admin' a second menu, intended for 'admin' only, will be printed
    # The options are to register a new user or view user statistics
    menu_2 = input(f"\nPlease select one of the following from the list:\n"
                   f"r - register new user\n"
                   f"s - view statistics\n"
                   f"e - exit\n")

    # A second nested if statement is used to either register a new user or print statistics
    # This if statement will be used to register a new user
    if menu_2 == "r":
        while True:

            # Variable 'new_username' is used to input the new username
            new_username = input("\nEnter a username: ")

            # The if statement checks if the new input username exists. If it does an error
            # message will inform the user the enter a different username
            if new_username == username:

                # If the username already exist in the txt file, the user will need to
                # enter another username
                print("This username already exist. Please enter another username.")

            else:

                # A nested while loop is used to add the new username and password to the file
                while True:

                    # Input variables needed to register a new user
                    new_password = input("Enter a password: ")
                    new_password_confirm = input("Please confirm your password: ")

                    # A nested if statement is used to verify that the password entered
                    # matches the confirmation password. If not, the loop will run again
                    # and ask the user to re-enter the password
                    if new_password != new_password_confirm:
                        print("\nYour password does not match. Please try again\n")

                    else:
                        # If the password confirmation is True, a confirmation message is printed
                        print("\nYour credentials are added to the database")

                        break  # If the password confirmation is True, the loop will end

                # The with/as statement opens the 'user.txt' file to store the new
                # username and password
                # The file is opened in append mode to add the info at the end of the list
                with open('user_2.txt', 'a+') as f:
                    f.write("\n" + new_username + ", " + new_password)

                break

        # After adding a new user, the user will be directed back to the user main menu
        user_main_menu()

        # No need to close a with/as statement as it automatically closes once the program
        # reaches the end of the block

    # The elif statement is used to check and print the statistics of the files
    elif menu_2 == "s":

        # The 'user.txt' file is opened in read mode to read the amount of users
        user_file = open("user_2.txt", "r")

        # Line count is set to zero, to be counted in the for loop below
        line_count = 0

        # This for loop block will check the amount of users
        # A for loop and 'line in' function is used to check if a line is empty.
        for line in user_file:

            # If the line in the file is not empty, the line count will increase by 1
            # until an empty line is reach.
            # The loop will then close.
            if line != "\n":
                line_count += 1

        user_file.close()  # The user_file needs to be closed after this block ends

        # The number of lines represents the number of users
        print("There are {} users currently registered".format(str(line_count)))

        # The 'task.txt' file is opened in read mode to read the amount of tasks
        task_file = open("tasks_2.txt", "r")

        # Line count is set to zero, to be counted in the for loop below
        line_count = 0

        # This for loop block will check the amount of tasks
        # A for loop and 'line in' function is used to check if a line is empty.
        for line in task_file:

            # If the line in the file is not empty, the line count will increase by 1
            # until an empty line is reached.
            # The loop will then close.
            if line != "\n":
                line_count += 1

        task_file.close()  # The task_file needs to be closed after this block ends

        # The number of lines represents the number of tasks
        print("There are {} tasks currently registered".format(str(line_count)))

    user_main_menu()


def add_task():
    # The file is opened in append mode
    with open("tasks_2.txt", "a+"):
        # All information needed to be stored in the 'tasks.txt' file, is retrieved
        # from the below variables
        task_title = input("What is the title of your task? ")
        task = input("What is the description of your task? ")
        start_date = input("Enter start date. Use format (yyyy/mm/dd) : ")
        due_date = input("Enter due date: Use format (yyyy/mm/dd) ")
        task_comp = "No"

    # This block will allow the program to update the task number without the user needing to
    # enter it
    with open("tasks_2.txt", "r+") as f:
        for line in f:
            line_num = line.split(",")
            num = int(line_num[0])
            task_number = num + 1

        # The f.write() function stores the input data in the following sequence
        # inside the 'task.txt' file
        f.write(f"\n{task_number}, {username}, "
                f"{task_title}, {task}, {start_date}, "
                f"{due_date}, {task_comp}")

        # A confirmation message is printed once all information is added to the 'tasks.txt' file
        print("\nYour task is added to the database")

    # The user is directed back to the user main menu without being logged out
    user_main_menu()


def view_all():
    log_in()

    # The Admin is permitted to view all information below
    # else:
    # The file is opened in read-only mode
    task_file = open("tasks_2.txt", "r")

    # The lines in the 'tasks.txt' file are split between the comma and open spaces,
    # using the .split() function, to print the information in separate lines as below
    for line in task_file:
        task_number, new_username, task_title, task, start_date, \
        due_date, task_comp = line.split(", ")

        # The information will be printed neatly as below in separate lines
        # The tab function '\t' is used to space the lines evenly
        print(f"""
                Task Number\t {task_number}
                Name:\t\t {new_username}
                Title:\t\t {task_title}
                Description:\t {task}
                Start Date:\t {start_date}
                End Date:\t {due_date}
                Task Complete:\t {task_comp}
                """)

    task_file.close()  # The task_file needs to be closed after this block ends

    # The user will be directed back to the user main menu
    admin_main_menu()


def view_mine():
    # The file is opened in read/ write mode
    global new_username, task_comp
    task_file = open("tasks_2.txt", "r+")

    # list_tasks = open("tasks_2.txt").readlines()

    # The lines in the 'tasks.txt' file are split between the comma and open spaces,
    # using the .split() function, to print the information in separate lines as below
    for line in task_file:
        task_number, new_username, task_title, task, start_date, \
        due_date, task_comp = line.split(", ")

        # This if statement will allow the current user to only view his/her information
        # if 'new_username' is equal to 'username'
        if new_username == username:
            # The information will be printed neatly as below in separate lines
            # The tab function '\t' is used to space the lines evenly
            print(f"""
            Task Number:\t {task_number}
            Name:\t\t {new_username}
            Title:\t\t {task_title}
            Description:\t {task}
            Start Date:\t\t {start_date}
            End Date:\t\t {due_date}
            Task Complete:\t {task_comp}
            """)

    # A nested menu is used to allow the user to open a specific task or return back to
    # the main menu
    vm_menu = input("\nPlease select one of the following options:"
                    "\n1. Open specific task\n"
                    "2. Enter '-1' to return to main menu\n")

    # After opening the specific task the user will have the option to edit that task
    # while True:

    # This if statement checks condition '1' which will allow the user to either
    # mark the task complete or edit it

    while True:

        if vm_menu == "1":
            number_vm = input("\nPlease enter a Task Number:\n")

            # The file 'task_2' is opened to access the information needed to
            # edit the selected task
            with open("tasks_2.txt", "r") as f:
                tasks_lines = f.read()

                int_number_vm = int(number_vm)

                # [(number_vm - 1)] reads position[0] in the line
                task_vm = tasks_lines.split("\n")[int_number_vm - 1]

            list_task_vm = [i for i in task_vm.split(", ")]

            # 'list_num' should be == number_vm and x (which is list_task_vm at position [6])
            # should be equal to 'No'
            list_num = int(list_task_vm[0])
            x = list_task_vm[6].strip("\n")

            # The if/and statement checks that both conditions are true. If one is False,
            # the user cannot edit the task
            if int_number_vm == list_num and username == list_task_vm[1]:

                # If both conditions above are true, the user is given two options of editing
                # the specific task
                if username == list_task_vm[1] and x != "Yes":
                    menu_edit = input("\nPlease select one of the following options:\n"
                                      "1. Mark task as complete\n"
                                      "2. Edit\n")
                    while True:

                        # Option 1 will mark the task as complete
                        if menu_edit == "1":

                            with open("tasks_2.txt", "r") as user_info:
                                data = user_info.readlines()

                                old_line = data[(int_number_vm - 1)]

                                # The replace() function will change 'No' to 'Yes' as required
                                # in option 1
                                new_line = old_line.replace("No", "Yes")

                                data[(int_number_vm - 1)] = new_line

                                print("\nYour task is marked as complete")
                                user_main_menu()

                            # The text file 'tasks_2' is opened in write mode to change 'No'
                            # to 'Yes'
                            with open("tasks_2.txt", "w") as user_info:
                                user_info.writelines(data)

                            break

                        # Option 2 will allow the user to either change the due date or change
                        # the user's username
                        elif menu_edit == "2":

                            edit_line = input("\nPlease select one of the following:\n"
                                              "1. Change due date\n"
                                              "2. Change username\n")

                            if edit_line == "1":

                                due_date_new = input("\nEnter new due date. Use format (yyyy/mm/dd): ")

                                # The file 'tasks_2' is opened in read mode
                                with open("tasks_2.txt", "r") as user_due_date:
                                    data = user_due_date.readlines()

                                    old_line = data[int_number_vm - 1]

                                    # The replace() function will change the due date in option 1
                                    # in position [5]
                                    new_line = old_line.replace(list_task_vm[5], due_date_new)

                                    # [(number_vm - 1)] reads potion[0] in the line
                                    data[int_number_vm - 1] = new_line

                                    print("\nYour due date is updated")
                                    user_main_menu()

                                    with open("tasks_2.txt", "w") as user_due_date:
                                        user_due_date.writelines(data)

                                    break

                            # Option 2 will allow the user to enter a new username
                            elif edit_line == "2":

                                username_update = input("\nEnter a new username: ")

                                # The file 'user_2' is opened in read mode
                                with open("user_2.txt", "r") as u_file:
                                    user_data = u_file.readlines()

                                    # An empty list is created to store the new username
                                    new_list_user = []

                                    for name in user_data:
                                        # The replace() function will change the old username
                                        # to the new username
                                        new_name = name.replace(username, username_update)
                                        new_list_user.append(new_name)

                                    # The write mode will add the new username to the text file
                                    with open("user_2.txt", "w") as u_file:
                                        u_file.writelines(new_list_user)

                                # The 'tasks_2' is opened in read mode
                                with open("tasks_2.txt", "r") as t_file:
                                    tasks_data = t_file.readlines()

                                    # An empty list is created to store the edited task in the
                                    # text file
                                    new_list_tasks = []

                                    # The replace() function will change the old username to the
                                    # new username
                                    for name in tasks_data:
                                        new_name = name.replace(username, username_update)
                                        new_list_tasks.append(new_name)

                                    # 'tasks_2' file is opened to write the new username to the file
                                    with open("tasks_2.txt", "w") as t_file:
                                        t_file.writelines(new_list_tasks)

                                print("\nYou've changed your username")
                                user_main_menu()

                                break

                        else:
                            print("Invalid option. Please try again")

                # If the task is complete, it cannot be edited
                else:
                    print("You cannot edit this task as it is complete")
                    user_main_menu()

                    break  # The break function ends the nested loop

            else:
                print("Invalid task number. Please try again")

                # If the username is incorrect, the loop will run again to allow the user
                # to enter the correct username
                continue

        elif vm_menu == "-1":
            user_main_menu()

        break
        # '-1' will direct the user back to the main menu

    task_file.close()  # The task_file needs to be closed after this block ends


def gen_report():
    import datetime
    today = datetime.date.today()
    complete = 0
    incomplete = 0
    overdue = 0

    if username != "Admin":
        print("You are not permitted view statistics")
        main_menu()

    else:

        print("\nTasks statistics\n")

        # Total tasks recorded
        line_count = 0
        with open("tasks_2.txt", "r") as f:
            for line in f:
                if line != "\n":
                    line_count += 1
        print("Total tasks recorded - " + str(line_count))

        # Tasks complete
        count = 0
        with open("tasks_2.txt", "r") as f:
            for line in f.readlines():
                words = line.lower().split()
                for word in words:
                    if word == "yes":
                        count += 1
        print("Total tasks complete - " + str(count))

        # Tasks incomplete
        tasks_incom = line_count - count
        print("Total tasks incomplete - " + str(tasks_incom))

        # Tasks overdue and incomplete
        with open("tasks_2.txt", "r") as f:
            for line in f:
                task_number, new_username, task_title, task, start_date, \
                due_date, task_comp = line.split(", ")

                due_date_obj = datetime.datetime.strptime(due_date, '%Y/%m/%d')
                task_due_date = (due_date_obj.date())

                d = task_comp.lower().strip("\n")

                if today > task_due_date and d == "no":
                    overdue += 1

                elif d == "yes":
                    complete += 1

                elif d == "no":
                    incomplete += 1

        # Tasks incomplete and overdue
        print("Tasks incomplete and overdue: " + str(overdue))

        # Tasks percentage incomplete
        tasks_percentage_incom = int((tasks_incom / line_count) * 100)
        print("Tasks percentage incomplete: " + str(tasks_percentage_incom) + "%")

        # Tasks percentage overdue
        tasks_percentage_overdue = int(((overdue / line_count) * 100))
        print("Tasks percentage overdue: " + str(tasks_percentage_overdue) + "%")

        task_overview_file = open("task_overview.txt", "r+")

        task_overview_file.write(f"Tasks Overview Statistics"
                                 f"\n"
                                 f"\nTotal tasks recorded - {line_count}"
                                 f"\nTotal tasks complete - {count}"
                                 f"\nTotal tasks incomplete - {tasks_incom}"
                                 f"\nTotal tasks incomplete and overdue -  {overdue}"
                                 f"\nTasks percentage incomplete - {tasks_percentage_incom}%"
                                 f"\nTasks percentage overdue - {tasks_percentage_overdue}%")

        task_overview_file.close()


def display_stats():
    import datetime

    # Imported datetime function is used to open today's date
    today = datetime.date.today()

    # An empty list and empty string is used to store new info inside it
    list_empty = []
    user_info = ""

    # Only the Admin is permitted to access the statistics of all the users
    if username != "Admin":
        print("You are not permitted to register a user")

    else:

        # The Admin is given a choice to access the statistics inside the text file
        # or on screen
        menu_ds = input(f"Please select one of the following:\n"
                        "1. Display user statistics in text file\n"
                        "2. Display user statistics on screen\n"
                        "3. Enter '-1' to return to main menu\n")

        # Option 1 will update and add the information inside the 'tasks_2' text file
        if menu_ds == "1":

            # 'user_overview_file' is opened in read/ write file to read an write info
            # the updated statistics inside it
            user_overview_file = open("user_overview.txt", "r+")

            # The 'truncate()' function is used to delete the info inside the text file
            # and append the updated info inside the file
            user_overview_file.truncate(0)
            user_overview_file.close()

            # Total users registered
            line_count_users = 0

            with open("user_2.txt", "r") as f:
                for line in f:
                    if line != "\n":
                        line_count_users += 1

            # Total tasks recorded
            line_count_tasks = 0

            with open("tasks_2.txt", "r") as f:
                for line in f:
                    if line != "\n":
                        line_count_tasks += 1

            # 'user_2' file is opened in read mode to read info
            with open("user_2.txt", "r") as f:
                for user_names in f:
                    line = user_names.split(", ")
                    list_empty.append(line[0])

            # The names are set to zero to increment it with 1 as the statistics
            # are updated
            f = open("tasks_2.txt", "r")
            for user_name in list_empty:
                user_num_tasks = 0
                user_tasks_comp = 0
                user_tasks_incomp = 0
                user_perc_tasks_comp = 0
                user_perc_tasks_incomp = 0
                user_tasks_overdue = 0
                y = 0

                # 'tasks_2' is opened to print the statistics, only accessed by Admin
                for line in f:
                    task_number, new_username, task_title, task, start_date, \
                    due_date, task_comp = line.split(", ")

                    # The username is updated in the list
                    if user_name in line:
                        user_num_tasks += 1

                        # Total tasks complete per user
                        if task_comp.lower().strip("\n") == "yes":
                            user_tasks_comp += 1

                        # Total tasks incomplete per user
                        elif task_comp.lower().strip("\n") == "no":
                            user_tasks_incomp += 1

                        # Total tasks per user
                        elif task_comp.lower().strip("\n"):
                            user_num_tasks = user_tasks_comp + user_tasks_incomp

                        # datetime function is used to check if a task is overdue
                        due_date_obj = datetime.datetime.strptime(due_date, '%Y/%m/%d')
                        task_due_date = (due_date_obj.date())

                        # Percentage tasks incomplete and overdue
                        if today > task_due_date and task_comp.lower().strip("\n") == "no":
                            y += 1
                            user_tasks_overdue = int((y / user_tasks_incomp) * 100)

                if not user_num_tasks == 0:
                    # Percentage tasks complete
                    user_perc_tasks_comp = int(((user_tasks_comp / user_num_tasks) * 100))

                    # Percentage tasks incomplete
                    user_perc_tasks_incomp = int(((user_tasks_incomp / user_num_tasks) * 100))

                    # The seek() function is used to used to run through the list from top
                    # down to the bottom
                    f.seek(0)

                user_overview_file = open("user_overview.txt", "r+")

                user_overview_file.write(f"\nUser Overview Statistics\n"
                                         f"\nTotal number of users is: {line_count_users}\n"
                                         f"Total number of tasks is: {line_count_tasks}\n")

                user_overview_file.close()

                user_overview_file = open("user_overview.txt", "a+")

                # The updated info is displayed in an ordered sequence useing new line
                # characters
                user_overview_file.writelines(f"\n{user_name}\n"
                                              f"Tasks complete: {user_tasks_comp}\n"
                                              f"Tasks incomplete: {user_tasks_incomp}\n"
                                              f"Total tasks: {user_num_tasks}\n"
                                              f"Percentage tasks complete: {user_perc_tasks_comp}%\n"
                                              f"Percentage tasks incomplete: {user_perc_tasks_incomp}%\n"
                                              f"Percentage tasks incomplete and overdue: {user_tasks_overdue}%\n")

            # The user is asked to open the text file to view the statistics
            print("\nOpen 'user_overview' text file to view statistics")

            user_overview_file.seek(0)

            # The admin is directed back to admin main menu
            admin_main_menu()

        # Option 2 will display the statistics on the screen
        elif menu_ds == "2":

            # 'user_overview_file' is opened in read/ write file to read an write info
            with open("user_overview.txt", "r+") as f:
                for line in f:
                    user_info += line
                print(user_info)

            # The admin is directed back to admin main menu
            admin_main_menu()

        # '-1' will send the user back to the main menu
        elif menu_ds == "-1":
            admin_main_menu()


# The two external files 'user_2.txt' and 'tasks_2.txt' are opened in read and write mode
# to retrieve and add data to
user_file = open("user_2.txt", "r+")
task_file = open("tasks_2.txt", "r+")
list_names = []

# 'file_access' is defined False to check the conditions in the loop to be true.
# Once all the conditions are met, will 'file_access' be true
file_access = False

# 'username' is defined as an empty string to store information in it
username = ""

# An infinite loop is created to keep on asking the user to enter the correct details,
# until it is True. The loop will then end.
while not file_access:  # Simplified expression. The 'while not' is the same as 'while file_access == False'

    # These two input variables will be used to unlock the program, if correctly typed, to use the menu below
    username = input("\nPlease type your username: ")
    password = input("Please type your password: ")

    for lines in user_file:

        # The split() function is used to remove the comma and empty string
        correct_user, correct_password = lines.split(", ")

        list_names_new = list_names.append(correct_user)

        # The if statement is used to check that both 'username' and 'password' is correct. This will make
        # 'file_access' True and the loop will end
        if username == correct_user and password == correct_password.strip("\n"):
            file_access = True

            if username == "Admin":
                admin_main_menu()

            else:
                user_main_menu()

            break  # The break function will end the loop once both conditions are True

    else:
        # The loop will continue to ask the user to re-enter the information until it is true
        print("\nYour username or password is incorrect, please try again")

    user_file.seek(0)  # The seek() function returns back to the beginning of the first line
    # to run the loop again until the condition is met, i.e. correct username and password

admin_main_menu()

# References:
# https://www.kite.com/python/answers/
# https://www.geeksforgeeks.org/python-seek-function/
# https://www.tutorialspoint.com/python/file_seek.htm
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# https://www.codegrepper.com/code-examples/python/external+files+in+python
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://www.w3schools.com/python/python_functions.asp
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_for_loops.asp
# HyperionDev Capstone Project III - Files Video
# https://www.delftstack.com/howto/python/read-first-line-in-python/
