"""
This block prints out basic details of the program

"""


print('This program will help you select your pet by giving information')
print('Select one Pet')
print('1. Cat')
print('2. Dog')
print('3. Horse')

pet=float(input("Please choose from one to three ")) #THIS LINE TAKES THE FIRST INPUT

"""
THIS BLOCK CONTAINS IF LOOPS WHICH DECIDE THE CONTROL FLOW AND OUTPUT

"""


if pet==1:
 print("Cats are essentially small predators which keep themselves around humans for their convenience.")
 cat=float(input('Which breed would you like 1. Persian 2. Ragdoll '))
 if cat==1:
     print('Persian Cats have a distinct face along with a rich and furry coat. The cost for one is 400gbp')
 elif cat==2:
     print('Ragdoll cats have a mix of light and dark colours on their coat.The cost for one is 350gbp')
 else:
     print('please re-run program and enter 1 or 2')
elif pet==2:
    print("They are loyal pets which are intelligent and obedient. ")
    dog = float(input('Which breed would you like 1. Huskey 2. Labrador '))
    if dog == 1:
        print('Huskey are found in cold weather and share similarity to wolves.The cost is 200gbp')
    elif dog == 2:
        print('Labradors are friendly dogs with a golden coat.The cost is 150gbp')
    else:
        print('please re-run program and enter 1 or 2')
elif pet==3:
    print("Horses are beautiful creatures which might be too expensive for some.")
    horse = float(input('Which breed would you like 1. Arabian 2. Mustang '))
    if horse == 1:
        print('Arabians are the fastest and most expensive type of horse. They cost 15000gbp')
    elif horse == 2:
        print('Mustangs are strong horses which are used for racing and farming.Cost is 10000gbp')
    else:
        print('please re-run program and enter 1 or 2')

else:
    print("Please re-run the program and select from 1, 2 or 3") #This line is for if user inputs things except 1,2 or 3
