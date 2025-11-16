num=input("enter number")
if(type(num)==str):
    print("enter number")
else:
 num=float(num)
 if(num>0):
     print("number is positive")
 elif(num<0):
     print("number is negative")
 else:
     print("number is zero")