#9.3
#1
"""
first=float(input('Enter first number: '))
second=float(input('Enter second number: '))
try :
    print(first/second)
except ZeroDivisionError:
    print('You cannot divide by zero')
  """
#2
"""
try:
    myfile = open("sample_text2.txt", "r")
    mytext = myfile.read()
    print(mytext)
    myfile.close()
except FileNotFoundError:
    print('File not found please use valid address')
"""
#9.4
#1
"""
try:
    word = input('Enter word: ')
    print(word)
    print("thank you")
except KeyboardInterrupt:
    print(99)
"""
#2
import math
angle=float(input('Enter angle: '))
try:
    print('sin of angle is',math.asin(angle))
except ValueError:
    print('you entered a value outside of arcsin domain')

