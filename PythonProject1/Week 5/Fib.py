"""
#Q1
def fib():
    num = int(input("How many terms do want to see of the fibonacci series: "))
    x = 0
    y = 1
    for i in range(num - 1):
        print(x)
        temp = y
        y += x
        x = temp



fib()
"""


#Q2
print("Password needs to have atleast one special, upper and lower case character.")
pass1=input("Enter Password Key ")
def passwordChecker(key):
    specials="!@# $%^&*()-+?_=,<>/\""
    specialchar=0
    lowercases=0
    uppercases=0

    if len(key) < 10:
        print("Password is too short must be at least 10 characters ")
        print("")
    for i in key:
        if i.islower():
            lowercases+=1
        elif i.isupper():
            uppercases+=1
        elif any(c in specials for c in key):
            specialchar+=1


    if lowercases==0 or uppercases==0:
        print("Password must have one uppercase letter or one lowercase letter")
        print("")
    if specialchar==0 :
        print("Password must have at least one special character")
    if specialchar!=0 and lowercases!=0 and uppercases!=0 and len(key)>10:
        print("")
        print("Your Password is strong ")

passwordChecker(pass1)


"""
#Q3
def atm():

    balance=0
    pin="2005"
    while True:

        print("")
        print("Welcome to the ATM please select the service ")
        print("")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice=input("Enter your choice ")
        if choice=="1":
            print("Balance is",balance)
        elif choice=="2":

            while True:
                pinInput = input("enter your pin ")
                if pinInput == pin:
                    withdraw = float(input("enter the amount you wish to withdraw: "))
                    balance -= withdraw
                    print("Your balance is:", balance)
                    break
                else:
                    print("Incorrect pin")
                    continue


        elif choice=="3":
            deposit=float(input("enter the amount you wish to deposit: "))
            balance+=deposit
            print("Your balance is:",balance)
        elif choice=="4":
            print("Thank you for using ATM")
            break
        else:
            print("Incorrect choice select from given options")
        if balance<0:
            print("Your balance is",balance,"you are in debt")

atm()
"""
