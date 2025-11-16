#Activity 2
"""
x=1
while x<=10:
    print(x)
    x+=1
"""
"""
x=-1
while x>=-10:
    print(x)
    x-=1
"""
"""
num1=float(input("enter number for table "))
for i in range(1,11):
        print(num1*i)
"""
"""
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if(i%5==0):
        if(i>500):
            break
        elif(i>150):
            continue
        else:
            print(i)
"""

#Activity 3
"""
for i in range(6):
    if(i==3 or i==6):
        continue
    else:
         print(i)
"""
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for n in numbers:

    if(n%2==0):
        even+=1
    else:
        odd+=1
print("we have",even,"even numbers and",odd,"odd numbers")
"""
"""
datalist = [1452, 11.23, 1 + 2j, True, 'www', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for i in datalist:
    print(i, type(i))
"""

#Activity 4
"""
num1=0
num2=1
while num1<50:
    print(num1)
    temp=num2
    num2+=num1
    num1=temp
"""
"""
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
"""
"""
digit=0
alphs=0
string1=input("enter string ")
for i in string1:
    if i.isdigit():
        digit+=1
    else:
        alphs+=1
print("we have",digit,"digits and",alphs,"alphabets")
"""
#Activity 5
"""
num=(int(input("enter number ")))
for i in range(1,num+1):
    print(i)
"""
"""
year = int(input("Enter a year: "))
if (year % 4) == 0:                  #if year is divisible by 4, it is a leap year
  if (year % 100) == 0:              #if year is divisible by 100 it will also be by 4
    if (year % 400) == 0:            #if year is divisible by 400 it will also be by 4
     print(year, " is a leap year")
    else:
     print(year, " is not a leap year")
  else:
       print(year, " is a leap year")
else:
      print(year, " is not a leap year")
"""
















