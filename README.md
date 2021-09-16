# Level-1-Capstone-Project-4
## User Task Manager
### This program involes two users, an admin and normal users, to register an account to add tasks assigned to the users.
### To add a task a user needs to create a username and password and log into their account to add tasks.
### There are two main menus, one for admin and one for users, where the user menu is limited to what options they can select. Below are the contents of the menus for the two users:
### *Admin Menu*
1. Register new user
2. Add task
3. View all tasks
4. View my tasks
5. Generate report
6. Display statistics
7. Exit
### *User Menu*
1. Register new user
2. Add task
3. View my tasks
4. Exit
### The menu options are discussed in more details as below:
### *1. Register new user*
* A username and password needs to be entered
* The password needs to be confirmed by entering it again.
* If the confirmation password does not mach, the user is asked to re-enter the password
* The user will be informed if the username entered already exists and that another username should be entered
* Once the username and password is registered, it will be saved to a text file called 'user_2.txt'
* A confirmation message will be displayed to inform the user that the task has been added to the database
### *2. Add task*
* The user needs to log in into his/her account
* A series of input data is needed to add a task
  - Title of the task
  - Description of the task
  - Enter start date
  - Enter due date
  - Is the task complete (The task will initially be marked as incomplete)
* Once the above info is entered, it will be saved to text file called 'tasks_2.txt'
* A confirmation message will be displayed to inform the user that the task has been added to the database
### *3. View all tasks*
* Only admin has access to view all tasks
* Each user's tasks will be displayed on screen in an easy to read manner, with all the information entered when registering a task
### *4. View mine*
* The ccurrent logged in user's tasks will be displayed on the screen
* The user is presented with a menu to either open a specific task or return back to the main menu
* If the user selects to open a specific task, he/she is presented with a second menu to either edit a specific task by selecting the task number or exit back to the main menu
* If the user selects to edit a specific task, the following options are given:
  - Mark task as complete
  - Change due date
  - Change username
* It should be noted that a task can only be edited if it is marked as incomplete
* If an invalid task number is entered the user will be informed and asked to re-enter a task number
* The user will be informed of all changes and it will be updated in the task file for that specific task
### *5. Generate report*
* Only admin has access to generate a report
* The following information will be generated and stored in a text file 'task_overview_file'
  - Total tasks recorded
  - Total tasks complete
  - Total tasks incomplete
  - Total tasks complete and overdue
  - Tasks percentage incomplete
  - Tasks percentage overdue
* By using the datetime.date.today() function, the task will automatically change to "overdue" if the date passes the intended due date
### *6. Display statistics*
* Only admin has access to disply statistics
* The admin is given a menu to choose the following options:
  - Display user statistics in text file
  - Display user statistics on screen
  - Enter '-1' to return to main menu
