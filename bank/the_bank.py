"""
Create an ATM-like program that helps customers create an account, review that account, make desposits and withdrawals, and more.

To show a Decimal as currency:
'${:,.2f}'.format(y)
"""
import os
import time
from decimal import Decimal
from bank_objects import *

customers = {}
# Customer dictionary: customer object as a key; value is a list of account
# objects associated with that customer. Going to leave customer as an
# attribute of account for now, but may not be necessary.

def clear_screen():
    # os.system('cls') # on windows
    os.system('clear')

# initial menu
def start_menu():
    print "Welcome to Python Community Credit Union!"
    print """Please choose from the following options:
    1. Log In (Returning Cusotmer)
    2. Sign Up (New Customers)"""

    choice = int(raw_input())
    if choice == 1:
        log_in()
    elif choice == 2:
        sign_up()
    else:
        clear_screen()
        start_menu()

# logging into the system
def log_in():
    print "Please provide the following information:"
    name = raw_input("Name on Account: ")
    pin = int(raw_input("Enter your PIN: "))
    # does name and PIN check out?
    customer_found = False
    for customer in customers:
        if customer.name == name and customer.pin == pin:
            cust = customer
            customer_found = True

    if customer_found == False:
        clear_screen()
        print "Incorrect information given. Please try again."
        log_in()
    else:
        # check to see if customer has multiple accounts
        
    # if just one account, continue with that
    # else, allow them to choose

# signing up for an account at our bank
def sign_up():
    print "To open an account with PCCC, please begin by providing the following information: "
    name = raw_input("Your full name: ")
    pin = raw_input("Choose a 4-digit PIN: ")

    cust = Customer(name,pin)

    customers[cust] = []

    clear_screen()
    account = new_account(cust)
    clear_screen()
    print "Account successfully created!"
    next_path(cust, account)

# find out how the customer wants to proceed
def next_path(customer, account):
    print """Would you like to...
    1. Continue with this Account
    2. Create Another Account
    3. Log Out of Session"""
    choice = int(raw_input())

    if choice == 1:
        account_menu(account)
    elif choice == 2:
        clear_screen()
        new_account(customer)
        print "Account successfully create!"
        next_path(customer, account)
    elif choice == 3:
        print "Thank you for your businesss. Good-bye!"
        time.sleep(5)
        start_menu()
    else:
        clear_screen()
        print "Invalid response. Try again."
        next_path(customer, account)

# creating a new account
def new_account(customer):
    acct_type = account_type()
    amount = Decimal(raw_input("How much would you like to initially deposit? $"))
    new_account = Account(customer, acct_type, amount)
    customers[customer].append(new_account)
    return new_account

# choosing an account type
def account_type():
    print """Please choose the type of account you'd like to open:
    1. Checking
    2. Savings
    3. Money Market"""

    choice = int(raw_input())
    if choice == 1:
        acct_type = "Checking"
    elif choice == 2:
        acct_type = "Savings"
    elif choice == 3:
        acct_type = "Money Market"
    else:
        clear_screen()
        print "Invalid response. Try again please."
        account_type()

    return acct_type

# what do to within account
def account_menu(account):
    clear_screen()
    print """Please choose from the following options:
    1. Make a Deposit
    2. Make a Withdrawal
    3. Change Your PIN
    4. Log Out"""

    choice = int(raw_input())
    if choice == 1:
        account.deposit
    elif choice == 2:
        account.withdrawal
    elif choice == 3:
        account.customer.change_pin
    else:
        print "Invalid response. Please try again."
        menu(account)

# cust = Customer("Jadzia", 1234)
# acct = Account(cust, "checking", 42)
#
# print "%s gains access thru the PIN # %d. They have a %s account with a balance of $%d" % (acct.customer.name, acct.customer.pin, acct.acct_type, acct.balance)

start_menu()
