class Account:
    def __init__(self, customer, acct_type, balance):
        self.customer = customer
        self.acct_type = acct_type
        self.balance = balance

    def deposit(self):
        print "How much would you like to deposit?"
        amount = float(raw_input("$"))
        self.balance += amount

    def withdrawal(self, amount):
        print "How much would you like to withdraw?"
        # overdraft protection
        if self.balance < 0:
            print "Insufficient funds. Sorry."
        else:
            amount = float(raw_input("$"))
            self.balance -= amount

class Customer:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

    def change_pin(self, pin):
        new_pin = raw_input("Enter a new four-digit pin: ")
        self.pin = new_pin
