#!/usr/bin/env python

#assuming bank as database
class Bank:
    firstName = "group"
    lastName = "02"
    code = "PSW2019GRP02"
    address = "AITILAB03"
    accountNo = "GRP0002"
    accountPin = 1234

    def manages(self):
        print("this is method manages under bank class")

    def maintains(self):
        print("this is the maintains method under the Bank class")

class ATM:
    location = None
    managedBy = None
    logIn_confirmation = None

    def __init__(self, accountNo, accountPin):
        self.accountNo = accountNo
        self.accountPin = accountPin

    def logIn(self):
        tries = 0
        while tries < 4:
            self.accountNo = str(input("ACCOUNT ID: "))
            self.accountPin = int(input("PIN: "))

            if (self.accountNo == Bank.accountNo) and (self.accountPin == Bank.accountPin):
                print("LOGIN SUCCESS")
                ATM.logIn_confirmation = True
                return ATM.logIn_confirmation
            else:
                print("INCORRECT LOGIN INFO, TRY AGAIN")
                tries += 1

                ATM.logIn_confirmation = False
                return ATM.logIn_confirmation

    def logOut(self):
        exit()

    def identifies(self):
        print("identifies method under ATM class")

    def transactions(self):
        print("transaction method under ATM class")

    def mainMenu(self):
        menuChoice = None

        if ATM.logIn_confirmation == True:
            while 1:
                print("WELCOME TO PSW2019 GROUP02 BANK ATM.")
                accountType = int(input("1: Savings\n 2: Checking\n "))
                
                if accountType == 1 or accountType == 2
                    print("1: CHECK BALANCE \n 2: DEPOSIT\n 3: WITHDRAW\n  4: LOG OUT\n")
                    menuChoice = int(input("enter your option: " ))
            
                    if (menuChoice == 1):
                        testAccount = Account("savings", "group02")
                        testAccount.checkBalance()
                    
                    
                    elif (menuChoice == 2):
                        testAccount = deposit_transaction()
                        testAccount.deposit()
                    
                    elif (menuChoice == 3):
                        testAccount = withdrawal_transaction()
                        testAccount.withdrawal()
                    
                    elif (menuChoice == 4):
                        ATM.logOut()
                    
        if ATM.logIn_confirmation == False:
            exit()

#under atm class
class atmTransaction:
    transactionID = None
    date = None
    type = None
    def update(self):
        print("this is the atm transaction class")
        #balance = balance - amount
        #return balance
        

class withdrawal_transaction(atmTransaction):
    # pin = 1234

    amount = None
    # def __init__(self, amount):
    #     self.amount = amount

    def withdrawal(self):
        amount = int(input("AMOUNT: "))
        if  amount <= Account.balance:
            new_balance = Account.balance - amount
            print(new_balance)
        else:
            print("INSUFFICIENT BALANCE")

class transfer_Transaction(atmTransaction):
    def __init__(self, amount,accountNo):
        self.amount = amount
        self.accountNo = accountNo

    def deposit(self):
        self.amount = float(input("AMOUNT: "))
        Account.balance = Account.balance + amount
        print("BALANCE: ", Account.balance)


#in association with Bank class
class debitCard:
    cardNo = None
    ownedBy = None

    def access(self):
        print("this is the debit Card class")

class Customer:
    name = Bank.firstName + " " + Bank.lastName
    address = Bank.address
    dob = "15-07-19"

    def owns(self):
        print("this is the customer class")

class Account:
    def __init__(self,type,owner):
        self.type = type
        self.owner = owner

    def checkBalance(self,accountNo):
        balance = 6000
        #link balance after withdrawal and deposit to balance somewhere so that
        # it can simply be inherited and kept up to date all the time
        print("Your balance is: ".format(balance))


    #account_type = input("1: Savings \n 2: Checking: ")

class Checking(Account):
    def __init__(self,accountNo):
        self.accountNo = accountNo

    def debit(self,accountNo):
        #is pin check necessary?
        #how do i make sure it's debiting from the right account?
        #Assumption: Debit account due to payment for bills,shopping,monthly deductions etc
        debitAmount = int(input("Enter amount: "))
        Account.balance = Account.balance - debitAmount
        print("{} has been deducted successfully from your account".format(debitAmount))

    def credit(self,accountNo,creditAmount):
        self.creditAmount = creditAmount

        print("Your account has been credited with {}".format(creditAmount))


class Savings(Account):
    def __init__(self,accountNo):
        self.accountNo = accountNo

    def debit(self,accountNo,debitNo):
        maxDebit = 6 #The maximum number of times an individual is allowed
        #to have their account debited
        #debitNo = number of debits done within the month
        if debitNo < 6:
            debitAmount = int(input("Enter amount: "))
            Account.balance = Account.balance - debitAmount
            print("{} has been deducted successfully from your account".format(debitAmount))
        else:
            print("You have exceeded your limit for the month.\n Please try again next month")


    def credit(self,accountNo,creditAmount):
        self.creditAmount = creditAmount

        print("Your account has been credited with {}".format(creditAmount))

group02ATM = ATM("GRP0002", 1234)
group02ATM.logIn()
group02ATM.mainMenu()
