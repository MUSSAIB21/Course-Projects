#Q1
num=float(input("enter number between 1 and 6 "))
if num==1:
    print("you guessed wrong")
elif num==2:
    print("you guessed wrong")
elif num==3:
    print("you guessed wrong")   
elif num==4:
    print("you guessed wrong")
elif num==5:
    print("you guessed wrong")
elif num==6:
    print("you are right")
else:
    print("Please Select Number Between 1 and 6")

#Q2
cel=float(input("Please Enter The Temperature In Celsius "))
print(f"The temperature in Kelvin is", cel+273,"K" )

#Q3
grade=int(input("enter grade "))
if(70<=grade<=100):
    print("Grade is A")
elif(60 <= grade <= 69):
    print("Grade is B")
elif(50 <= grade <= 59):
    print("Grade is C")
elif(45 <= grade <= 49):
    print("Grade is D")
elif(40 <= grade < 44):
    print("Grade is E")
elif(0 <= grade < 39):
    print("Resit")
else:
    print("Enter Integer between 0 and 100")
