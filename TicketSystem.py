from getpass import getpass
import platform
import os
from time import sleep
from random import randint

# https://replit.com/@DillusionersTeam/TicketSystem#main.py

# function to clear the terminal
def clear():
    # if the os is Windows, then run 'cls', else run 'clear'
    if platform.system() == 'Windows':
        os.system('cls')

    else:
        os.system('clear')

# a class to create a Ticket System with a login menu
class TicketSystem:
    # class constructor
    def __init__(self):
        # checks if someone is currently logged in or not
        self.logged_in = False

        # stores the username and password of the currently logged user
        self.logged_account = ['', '']

        # stores all the accounts that are registered
        # key and values are both str
        self.accounts = {}

        # stores the tickets of all the registered accounts
        # keys -> str, value -> list of str
        self.tickets = {}

        # amount of time spent on the sleep() function in time package
        self.waiting_duration = 2

    # function to register the user
    def register(self):
        print('REGISTER PAGE\n')

        # user input for name
        name = input('Enter your username: ')

        # if there is already an account with the given name
        if name in self.accounts.keys():
            print('An account with this name already exists. Please log in to access the account.')
            sleep(self.waiting_duration)
            return

        # user input for password
        password = getpass(prompt='Enter your password: ')

        # storing the register details in accounts dict
        self.accounts[name] = password

        # creating a new ticket for the given user
        self.tickets[name] = []

        # changing the logged account to the currently registered account
        self.logged_account = [name, password]

        print('Successfully registered your account!')

        # now the user is logged in
        self.logged_in = True
        sleep(self.waiting_duration)

    # logs in the user if they have an already existing account
    def login(self):
        print('LOGIN PAGE\n')

        # user name input
        name = input('Enter your username: ')
        acc_password = ''

        # if there is no username in the accounts dict
        if not name in self.accounts.keys():
            print('There is no account with this given username. Please try again.')
            sleep(self.waiting_duration)
            return

        else:
            # accessing the account password
            acc_password = self.accounts[name]

        # user input for password
        password = getpass(prompt='Enter your password: ')

        # if the given password is equal to the original password
        if acc_password == password:
            print('Successfully logged in to your account.')
            self.logged_account = [name, password]

        else:
            print('Incorrect password provided. Please try again later.')

        # changing the login state based on the given condition
        self.logged_in = (acc_password == password)
        sleep(self.waiting_duration)

    # logging out the user from their account
    def logout(self):
        print('LOGOUT PAGE\n')

        # setting the logout variable to false
        self.logged_in = False

        # clearing the currently logged user
        self.logged_account = ['', '']

        print('Successfully logged out!')
        sleep(self.waiting_duration)
        
    # creating a new ticket
    def create_ticket(self):
        print('TICKET CREATION PAGE\n')
        ticket_id = ''

        # creating a new ticket id for the ticket
        for _ in range(10):
            ticket_id += str(randint(0, 9))

        # storing the ticket in the logged account
        self.tickets[self.logged_account[0]].append(ticket_id)

        print(f'Successfully created a ticket with ID {ticket_id}')
        sleep(self.waiting_duration + 3)

    # deleting an existing ticket
    def delete_ticket(self):
        print('TICKET DELETION PAGE\n')

        # user input for ticket
        ticket_id = input('Enter your Ticket ID: ')

        # checking if the given ticket exists
        if not ticket_id in self.tickets[self.logged_account[0]]:
            print('There is no ticket with this given Ticket ID. Please try again.')
            sleep(self.waiting_duration)
            return
        
        # removing the ticket from the logged accounts list
        self.tickets[self.logged_account[0]].remove(ticket_id)

        print('Successfully deleted the Ticket.')
        sleep(self.waiting_duration)

    # view all tickets for the currently logged account
    def view_tickets(self):
        print('VIEW TICKETS PAGE\n')
        print('The tickets are as follows:\n')

        # iterating through all of the tickets for the logged user and printing them
        for id in self.tickets[self.logged_account[0]]:
            print(id)
        
        # null input
        input('\nPress [ENTER] to continue......')

    # the main function of the program
    def main(self):
        # infinite loop until the user exits out
        while 1:
            clear()

            # if the user is not logged in
            if not self.logged_in:
                # printing the menu
                print('Welcome User! Choose any of the following options:')
                print('1. Register\n2. Login\n3. Exit')
                choice = input('>> ')
                clear()

                # match-case based on user choice
                match choice:
                    # register
                    case '1':
                        self.register()

                    # login
                    case '2':
                        self.login()

                    # exit
                    case '3':
                        print('Exitting the program....')
                        break
                    
                    # default case
                    case _:
                        print('Invalid choice!')
                        sleep(self.waiting_duration)

            # if the user is logged in
            else:
                # printing the menu
                print(f'Welcome {self.logged_account[0]}! Choose any of the following options:')
                print('1. Create Ticket\n2. View Tickets\n3. Delete a ticket\n4. Logout\n5. Exit')
                choice = input('>> ')
                clear()

                # match-case based on user choice
                match choice:
                    # create a ticket
                    case '1':
                        self.create_ticket()

                    # view tickets
                    case '2':
                        self.view_tickets()

                    # delete tickets
                    case '3':
                        self.delete_ticket()

                    # logout
                    case '4':
                        self.logout()

                    # exit
                    case '5':
                        print('Exitting the program.....')
                        break

                    # default case
                    case _:
                        print('Invalid Choice!')
                        sleep(self.waiting_duration)

        
# if the file is run and not imported from any other file
if __name__ == '__main__':
    # creating an object of the TicketSystem class and running the main function
    t = TicketSystem()
    t.main()
