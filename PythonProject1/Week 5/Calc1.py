print("Hello this is a calculator program which will do operations on 2 numbers you enter ")
def oInput():
    print("Enter + - * / % to perform the respective operations and x or X to stop program")
    o=input("Enter the operation you want to perform: ")
    return o
def numInput():
    number=input("Enter the number  : ")
    return number
def calc():
    while True:
        x=numInput()

