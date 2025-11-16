""""

ACTIVITY 1(In class notes)

words = ['cat', 'window', 'defenestrate']
for w in words:
 print(w, len(w))
 #This code first prints the String in list words at index w and also prints its length
"""
"""
for l in 'Jhon':

     if l != 'o':
         pass
         print(l, end=", ")
"""
"""
for num in range(-2,-5,-1): 

    print(num, end=", ")
    
  """
"""
x = 0

while (x < 100):

  x+=2

print(x)
"""
"""
x = 0

a = 0

b = -5

if a > 0:

    if b < 0:

        x = x + 5

    elif a > 5:

        x = x + 4

    else:

        x = x + 3

else:

    x = x + 2

print(x)

"""
"""
i = 1

while i < 6:

  print(i)

  if i == 3:

    break

  i += 1

"""
""""
i = 0

while i < 6:

  i += 1

  if i == 3:

    continue

  print(i)
"""
""""
i = 1

while i < 6:

  print(i)

  i += 1

else:

  print("i is no longer less than 6") 
"""
"""
list1 = [10, 20, 30, 40, 50]
size = len(list1) - 1

for i in range(size, -1, -1):
    print(list1[i], end=" ")
"""
"""
num = 75869

count = 0

while num != 0:

    # floor division

    # to reduce the last digit from number

    num = num // 10

    # increment counter by 1

    count = count + 1

print("Total digits are:", count) 
"""
"""
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# stat from index 1 with step 2( means 1, 3, 5, and so on)

for i in my_list[1::2]:

    print(i, end=" ")
    """
"""
input_number = 6

for i in range(1, input_number + 1):

    print("Current Number is :", i, " and the cube is", (i * i * i)) 
"""
"""
i = 0
product = 1
count = int(input("Enter the number of real numbers: "))
for i in range(count):

    x = float(input("Enter a real number: "))
    product = product * x
print(product)
"""