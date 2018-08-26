"""
Create an ATM-like program that helps customers create an account, review that account, make desposits and withdrawals, and more.
"""
import os
import time
from bank_objects import *

def menu(account):
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

cust = Customer("Jadzia", 1234)
acct = Account(cust, "checking", 42)

print "%s gains access thru the PIN # %d. They have a %s account with a balance of $%d" % (acct.customer.name, acct.customer.pin, acct.acct_type, acct.balance)
