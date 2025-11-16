
import math  # This imports math class which we will be using

print("Hello this is a calculator program which will do operations on 2 numbers you enter ")

""" 
This is the first function which is called oInput, the purpose of this function is to receive 
the operator input. It prints out the sign prompt, receives the input and finally,  
returns it to where its called. 
"""


def oinput():
    while True:
        print(
            "Enter + - * / % to perform the respective operations, x or X to stop program and sin,cos for sine and cosine functions")
        o = input("Enter the operation you want to perform: ")

        if o.strip() == "+" or o.strip() == "-" or o.strip() == "*" or o.strip() == "/" or o.strip() == "%" or o.strip() == "x" or o.strip() == "X" or o.strip() == "**" or o.strip() == "sin" or o.strip() == "cos":
            return o.strip()  # The .strip function ignore
        else:
            print("")
            print("Please enter valid operator and try again ")
            print("")
        """ 
       The oInput function gives a warning if you enter anything except the valid operators 
       and gives another prompt for you to  try again incase you enter an invalid operator. 

       """


""" 
This function is called calculator, and unlike our previous function, this does not return any 
value, it only executes the code. This function is where most of our code regarding the 
calculations is. 
"""


def calculator():
    """
            The next lines call the function oInput and store the value it returns into a new
            variable named op
    """
    while True:
        print("")
        op = oinput()
        print("")
        """ 
       The below lines deal with trigonometric functions in which 
       we can enter value in radians and degrees. We use the math class we imported 
       """

        if op == "sin":
            unit = float(input("Enter the unit of the number: 0 for degree and 1 for radians: "))
            if unit == 0:
                deg = float(input("Enter the angle in degree: "))
                print("The answer is ", math.sin(math.radians(deg)))
                continue
            elif unit == 1:
                rad = float(input("Enter the angle in radians: "))
                print("The answer is ", math.sin(rad))
                continue
            else:
                print("Please enter a valid unit or try again ")
        elif op == "cos":
            unit = float(input("Enter the unit of the number: 0 for degree and 1 for radians: "))
            if unit == 0:
                deg2 = float(input("Enter the angle in degree: "))
                print("The answer is ", math.cos(math.radians(deg2)))
                continue
            elif unit == 1:
                rad2 = float(input("Enter the angle in radians: "))
                print("The answer is ", math.cos(rad2))
                continue
            else:
                print("Please enter a valid unit or try again ")
        elif op == "x" or op == "X":
            print("Thanks for using the program")
            break
        """ 
       These lines are for receiving the two input numbers for arithmetic operations. 
       They assign them to variables named first and second. 
       """
        print("")

        first = input("Enter First Number: ")
        try:
            first=float(first)
        except ValueError:
            print("Please enter a valid number or try again ")
            continue
        second = input("Enter Second Number ")
        try:
            second=float(second)
        except ValueError:
            print("Please enter a valid number or try again ")
            continue

        """ 
       We now have if statements which determine the answer based on the sign used as the 
       operator. + is for addition, - for subtraction, * for multiplication, / for division 
       and % for modulus operation. 
       """

        if op == "+":
            print("The sum is ", first + second)
        elif op == "-":
            print("The difference is ", first - second)
        elif op == "**":
            print("The answer is ", first ** second)
        elif op == "*":
            print("The product is ", first * second)
        elif op == "/":
            if second != 0:
                print("The quotient is ", first / second)
            else:
                try:
                    print("The quotient is ", first / second)
                except ZeroDivisionError :
                    print("Cannot Divide by zero, please enter another number.")
        elif op == "%":
            print("The remainder is ", first % second)
        elif op == "x" or op == "X":
            """ 
           This operation is used to stop our program and is triggered by entering  
          x or X as input for operator. It breaks the while loop 
           """
            print("Thank you for using this program")
            break

try:
    calculator()
except KeyboardInterrupt:
    print("\n\nProgram terminated by user")
""" 
We use the final line to call the calculator function 
"""

