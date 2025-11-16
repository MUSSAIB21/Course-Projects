list1=[-10,10,4,-20,6,-7,-3]
list2=[]      #We create another list to store the positive elements of the original list

def posadder(): #Defining the function
    for i in list1: #This for loops iterates over the numbers in list1
        if i>0:           #This if condition adds the positive elements of list1 to list2
            list2.append(i)
    print(sum(list2))               #prints the sum
posadder()















