from getpass import getpass
from platform import system as sys
from os import system
from sys import stderr, stdout
from time import sleep

# https://replit.com/@DillusionersTeam/TodoList#main.py

# function to clear the terminal
def clear():
    # if the os is Windows, then run 'cls', else run 'clear'
    if sys() == 'Windows':
        system('cls')

    else:
        system('clear')

# function to reduce syntax in the main program
def sleeping_print(text: str, file = stdout, duration: int = 2):
    print(text, file=file)
    sleep(duration)


# class for account system in the Todo list
class LoginSecurity:
    # constructor
    def __init__(self):
        # stores whether the user is currently logged in or not
        self.logged_in = False

        # stores the username of the currently logged used
        self.current_user = ''

        # stores all user accounts
        # key -> string (username), value -> string (password)
        self.accounts = {}
        
    # function to register accounts
    def register(self):
        print('REGISTRATION PAGE\n')

        # username input
        name = input('Enter your username: ')

        # if there is already an account with the given username or name is empty
        if name in self.accounts or name == '':
            sleeping_print('ERROR: This account already exists.', file=stderr)
            return
        
        # getting the password
        password = getpass('Enter your password: ')

        # if password is shorter than six characters
        if len(password) < 6:
            sleeping_print('ERROR: Password cannot be lesser than 6 characters.', file=stderr)
            return
        
        # creating new account and logging in the user
        self.accounts[name] = password
        self.current_user = name
        self.logged_in = True

        sleeping_print('Successfully registered your account.')

    # function to login to an existing account
    def login(self):
        print('LOGIN PAGE\n')

        # username input
        name = input('Enter your username: ')

        # if the name is empty or the name is not logged in already
        if not name in self.accounts or name == '':
            sleeping_print('ERROR: Account with specified name doesnot exist.', file=stderr)
            return
        
        # password input
        password = getpass('Enter your password: ')

        # if the input password is equal to the original password
        if password == self.accounts[name]:
            sleeping_print('Successfully logged in.')
            self.logged_in = True
            self.current_user = name

        # if wrong password is given
        else:
            sleeping_print('ERROR: Incorrect Password.', file=stderr)

    # logging out of existing account
    def logout(self):
        print('LOGOUT PAGE\n')

        # verifying if the user is sure about their decision
        surity = input('Are you sure you want to log out? (y/n): ') == 'y'

        # if the user is sure
        if surity:
            # logging out
            self.logged_in = False
            self.current_user = ''

            sleeping_print('Successfully logged out of your account.')
            return
        
        # if the user is unsure
        sleeping_print('Aborting your choice.')

    # function to delete user accounts
    def delete_account(self):
        print('ACCOUNT DELETION PAGE\n')

        # verifying if the user is sure about their decision
        surity = input('Are you sure you want to delete account? (y/n): ') == 'y'

        # if the user is sure
        if surity:
            # removing the account from the 'accounts' dict
            self.accounts.pop(self.current_user)
            self.logged_in = False
            self.current_user = ''

            sleeping_print('Successfully deleted your account.')
            return
        
        # if the user is unsure
        sleeping_print('Aborting your choice.')


# class for the Todo List program 
class TodoList(LoginSecurity):
    # class constructor
    def __init__(self):
        # running the constructor of the LoginSecurity class
        super().__init__()

        # stores the tasks for all the users
        # key -> string (usernames), value -> list (all the tasks for the user)
        self.todos = {}

        # lambda function to verify if a task number is valid or not
        self.valid_task_number = lambda task_num : task_num < len(self.todos[self.current_user]) and task_num >= 0

    # function to create a new task
    def create_task(self):
        print('TASK CREATION PAGE\n')

        # task name input
        task_name = input('Enter the name of the task: ')

        # if the task already exists
        if task_name in self.todos[self.current_user]:
            sleeping_print('ERROR: Task already exists.', file=stderr)
            return

        # adding the new task to the user
        self.todos[self.current_user].append(task_name)
        sleeping_print('Successfully added your task.')

    # function to view all tasks for the currently logged in user
    def view_tasks(self):
        print('VIEW TASK PAGE\n')
        print('Your tasks are as follows:\n')
        
        # variable to number the task numbers
        itr = 1

        # iterating through all the tasks
        for task in self.todos[self.current_user]:
            # printing the task and updating 'itr' variable
            print(f'{itr}. {task}')
            itr += 1

        input('\nPress [ENTER] to continue......')
    
    # function to remove a task from the list
    # first_task -> boolean value which, when true, removes the first task from the list
    def pop_task(self, first_task: bool = False):
        print('REMOVE TASK MENU\n')

        # if the first task is to be removed
        if first_task:
            # asking the user if they are sure
            surity = input('Are you sure you want to remove the first item? (y/n): ') == 'y'

            # if the user is sure and the tasks list is not empty
            if surity and len(self.todos[self.current_user]) != 0:
                self.todos[self.current_user].pop(0) # removing the first task
                sleeping_print('Successfully removed the latest task in the list.')
                return
            
            # if the user is unsure
            sleeping_print('Aborting your choice.')
            return

        # task number input from user
        task_number = int(input('Enter the task number (see View Tasks Page): ')) - 1

        # if the task number is not valid
        if not self.valid_task_number(task_num=task_number):
            sleeping_print('ERROR: Task does not exist in the list.', file=stderr)
            return
        
        # removing the task with the specified index
        self.todos[self.current_user].pop(task_number)

        sleeping_print('Successfully removed the specified task.')

    # function to clear all tasks for the user
    def clear_tasks(self):
        print('CLEAR TASKS MENU\n')

        # asking the user if they are sure
        surity = input('Are you sure you want to clear all tasks? (y/n): ') == 'y'

        # if the user is sure
        if surity:
            # clearing the list
            self.todos[self.current_user] = []

            sleeping_print('Successfully cleared all tasks.')
            return
        
        # if the user is unsure
        sleeping_print('Aborting your choice')

    # function to reorder two tasks
    def reorder_task(self):
        print('TASK REORDER PAGE\n')

        # task number for the first task input
        first_task_number = int(input('Enter the task number of the first task: ')) - 1
        
        # if the task number is not valid
        if not self.valid_task_number(task_num=first_task_number):
            sleeping_print('ERROR: Task does not exist in the list.', file=stderr)
            return
        
        # task number for the second task input
        second_task_number = int(input('Enter the task number for the second task: ')) - 1

        # if the second task number is invalid
        if not self.valid_task_number(task_num=second_task_number):
            sleeping_print('ERROR: Task does not exist in the list.', file=stderr)
            return

        # swapping the values of the two tasks
        temp = self.todos[self.current_user][second_task_number]
        self.todos[self.current_user][second_task_number] = self.todos[self.current_user][first_task_number]
        self.todos[self.current_user][first_task_number] = temp

        sleeping_print('Successfully reordered your tasks.')

    # main function of the program
    def main(self):
        # infinite loop until the user stops it
        while 1:
            clear()
            print('MAIN MENU\n')

            # if the user is not logged in
            if not self.logged_in:
                # printing the menu
                print('Welcome User! Please choose any of the following options: ')
                print('1. Register\n2. Login\n\n3. Exit\n')
                choice = input('>> ')
                clear()

                # match-case based on user choice
                match choice:
                    # register
                    case '1':
                        self.register()

                        # creating a new list for the registered user
                        self.todos[self.current_user] = []

                    # login
                    case '2':
                        self.login()

                    # exit
                    case '3':
                        print('Exitting from the program....')
                        break
                    
                    # default
                    case _:
                        sleeping_print('ERROR: Invalid choice.', file=stderr)

            # if the user is logged in
            else:
                # printing the menu
                print(f'Welcome {self.current_user}! Please choose any of the following options: ')
                print('1. View All Task\n2. Create Task\n3. Remove First Task\n4. Remove a Task\n5. Reorder Tasks')
                print('6. Clear All Tasks\n\n7. Logout\n8. Delete Account\n\n9. Exit\n')
                choice = input('>> ')
                clear()

                # match-case based on user choice
                match choice:
                    # view all tasks
                    case '1':
                        self.view_tasks()

                    # create a new task
                    case '2':
                        self.create_task()
                    
                    # removing the first task
                    case '3':
                        self.pop_task(True)

                    # removing a task for the given index
                    case '4':
                        self.pop_task()

                    # reorder tasks
                    case '5':
                        self.reorder_task()

                    # clearing all tasks
                    case '6':
                        self.clear_tasks()

                    # logging out
                    case '7':
                        self.logout()

                    # delete account
                    case '8':
                        self.delete_account()

                    # exit program
                    case '9':
                        print('Exitting the program.......')
                        break
                    
                    # default
                    case _:
                        sleeping_print('ERROR: Invalid choice.', file=stderr)


# running the program
if __name__ == '__main__':
    # creating a new object for the TodoList class
    todo_app = TodoList()

    # running the main method
    todo_app.main()
