
#Q1
"""
def sorter(list2):

    print(sorted(list2))
"""
#Q2
"""
def intersector(list1, list2):
    return set(list1)&set(list2)
"""
#Q3
"""
def sumAvg(list1):
    print(sum(list1))
    print (sum(list1)/len(list1))
"""
#Q4
"""
fruits=["apples","pears","oranges","bananas"]
fruits.append("grapes")
"""
#Q5
"""
myTuple=("abc0", "sad",2,4)
print(myTuple[2])
"""
#Q6
"""
myList=[1,2,4,5,6,7]
print()
sortedList=sorted(myList)
print(sortedList[0],"is the smallest element in the list")
print(sortedList[len(sortedList)-1],"is the largest element in the list")
"""
#Q7
"""
def squaredList(list1):
    newList=[]
    for i in list1:
        newList.append(i*i)
    return newList
list2=[1,2,4,5,6,7]
print(squaredList(list2))
"""
#Q8
"""
list1=[1,2,4,5,6,7,"ab","ab"]
for i in list1:
    print(i,"is in list",list1.count(i),"times")
"""
#Q9
"""
list1=[4,5,3,64,6,5]
list2=sorted(list1)
if list1==list2:
    print("list1 is in ascending order")
else:
    print("list1 is not sorted in ascending order")
"""
#Q10
"""
def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unionSet = set1|set2
    return list(unionSet)
list_b = [4, 5, 3, 64, 6, 5, 2]
list_a = [5, 3, 77, 3, 8]
print(union(list_a, list_b))
"""

#Q11
"""

personDictionary={
    'name':"Mathew",
    'age':18,
    'address':"king's street"
}
"""
#Q12
"""
dict1={
    'name':'Mathew',
    'age':18,
    "address":"king's street"

}
dict2={
    'phone':"07446785335",
    'occupation':'doctor',
    'income':100000
}

dict1.update(dict2)
print(dict1)
"""
"""
#Q13
set1={1,2,3,5,6,"abc","abd",'a'}
set2={1,3,4,7,"abc","raf",'a'}
if set1&set2==set():
    print("the two sets have noting in common")
else:
    print("the sets have elements",set1&set2,"in common")
"""
"""
#Q14
set1={1,2,3,5,6,"abc","abd",'a'}
set2={1,3,4,7,"abc","raf",'a'}
print('set1-set2 =',set1-set2)
print('set2-set1 =',set2-set1)
print('intersection is ',set1&set2)
print('union is ',set1|set2)
"""
#Q15
"""
s0tring1="abcdef*g"
string2="zabwgf&*"
uniqueList=[]
for i in string1:
    for j in string2:
        if i==j:
            uniqueList.append(i)
print(uniqueList)
"""





