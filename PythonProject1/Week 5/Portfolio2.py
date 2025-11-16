print("Hello this is a calculator program which will do operations on 2 numbers you enter ")


while True:
    print("")
    first= float(input("Enter the first number: "))
    second= float(input("Enter the second number: "))
    print("")
    print("Enter + - * / % to perform the respective operations and x or X to stop program")
    op = input("Enter the operation: you wish to perform ")
    print("")
    if op=="+":
        print("The sum is ",first+second)
    elif op=="-":
        print("The difference is ",first-second)
    elif op=="*":
        print("The product is ",first*second)
    elif op=="/":
        print("The quotient is ",first/second)
    elif op=="%":
        print("The remainder is ",first%second)
    elif op=="x" or op=="X":
        break
    else:
        print("The operator is invalid please enter valid operator")
