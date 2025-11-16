"""
#Q1
def cAr():
    rad=float(input())
    print(rad*rad * 3.14)
cAr()
"""
"""
#Q2
def isPrime():
    num=int(input("Enter the number: "))
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")

isPrime()
"""
"""
#Q3
def reverse_string(text):
    return text[::-1]
input_str = input("Enter the string you want to reverse: ")
reversed_str = reverse_string(input_str)
print("reversed string is ",reversed_str)
"""
"""
#Q4
list1= [-2,2,-1,1,0]
def adder(vList):
    list2=[]
    for i in vList:
        if i>0:
            list2.insert(0,i)
    print(sum(list2))

adder(list1)
"""
"""
#Q5
word1=input("Enter the word: ")

def palCheck(word):

    rword = word[::-1]
    if rword == word:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")
palCheck(word1)
"""

"""
#Q6
list1=[2,3,4,5]
for i in list1:
    print(i*i)
"""
"""
#Q7
def mulTable():
    num=int(input("Enter the number: "))
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
mulTable()
"""
"""
#Q8
year=int(input("Enter the year: "))
def leapYear():
    if year%4 ==0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
leapYear()
"""
"""
#Q9
def evenodd():
    num=int(input("Enter the number: "))
    if num%2==0:
        print("EVEN")
    else:
        print("ODD")
evenodd()
"""

"""
#Q10
def mulTable2():
    num=int(input("Enter the number: "))
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
mulTable2()
"""

